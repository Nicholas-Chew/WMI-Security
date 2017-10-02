# Permanent WMI Event Subscriptions
## Finding the WMI Instances
We can use Get-WMIObject with the –Class parameter consisting of root\Subscription and then specifying the appropriate class that we wish to view.
```
#List Event Filters
Get-WMIObject -Namespace root\Subscription -Class __EventFilter
```
You can tell what kind of query is being used by the Query property of the Filter instance.
```
#List Event Consumers
Get-WMIObject -Namespace root\Subscription -Class __EventConsumer
```
From the Binding you can see what Consumer is being used and what exactly is being used in the other properties.
```
#List Event Bindings
Get-WMIObject -Namespace root\Subscription -Class __FilterToConsumerBinding
```

## Event & Consumer Creation
### Option #1: Using [wmiclass]
#### Event Filter
The first method of creating the WMI event subscription is by taking advantage of the wmiclass type accelerator and using the CreateInstance() method. First I will start off by creating the instance of the Filter.
```
#Creating a new event filter
$instanceFilter = ([wmiclass]"\\.\root\subscription:__EventFilter").CreateInstance()
```
Put the required parameter such as QuaeyLanguage, Query, Name & EventNameSpace 
```
$instanceFilter.QueryLanguage = "WQL"
$instanceFilter.Query = "select * from __instanceModificationEvent within 5 where targetInstance isa 'win32_Service'"
$instanceFilter.Name = "ServiceFilter"
$instanceFilter.EventNamespace = 'root\cimv2'
```
You cannot see the full member by using Get-Member, have to use -View All to see. Put method is the method to actually save this instance into the WMI repository.
```
$instancefilter | Get-Member -View All
```
Put method to save this instance. It will output an object that I will need to hold onto so I can use it’s Path property later on for the Binding.
```
$result = $instanceFilter.Put()
$newFilter = $result.Path
```
#### Consumer
```
#Creating a new event consumer
$instanceConsumer = ([wmiclass]"\\.\root\subscription:LogFileEventConsumer").CreateInstance()
```
Configure the object to create a log file whenever the Filter has fired
```
$instanceConsumer.Name = 'ServiceConsumer'
$instanceConsumer.Filename = "C:\Scripts\Log.log"
$instanceConsumer.Text = 'A change has occurred on the service: %TargetInstance.DisplayName%'
```
we need to save the object into the WMI repository and retain the path for binding usage.
```
$result = $instanceConsumer.Put()
$newConsumer = $result.Path
```
#### Binding
```
#Bind filter and consumer
$instanceBinding = ([wmiclass]"\\.\root\subscription:__FilterToConsumerBinding").CreateInstance()
```
Now bind the Filter and the Consumer together and save the instance
```
$instanceBinding.Filter = $newFilter
$instanceBinding.Consumer = $newConsumer
$result = $instanceBinding.Put()
$newBinding = $result.Path
```
#### Removing event, consumer and binding
```
##Removing WMI Subscriptions using [wmi] and Delete() Method
([wmi]$newFilter).Delete()
([wmi]$newConsumer).Delete()
([wmi]$newBinding).Delete()
```
By giving the path of the instance, the [wmi] type accelerator will cast it out to the proper type. This also means that you have access to the Delete() method and can easily remove all of the subscription instances without any issues.

### Option #2: Using Set-WMIInstance
This method makes use of the –Arguments parameter which accepts a hashtable that will be used to define each instance and its properties. This method also lends itself very nicely to “splatting”.

First, create the hash table that will be used with my splatting and these are also the common parameters which will not be changed with each WMI instance.
```
#Set up some hash tables for splatting
$wmiParams = @{
    Computername = $env:COMPUTERNAME
    ErrorAction = 'Stop'
    NameSpace = 'root\subscription'
}
```

#### Filter
```
#Creating a new event filter
$wmiParams.Class = '__EventFilter'
$wmiParams.Arguments = @{
    Name = 'ServiceFilter'
    EventNamespace = 'root\CIMV2'
    QueryLanguage = 'WQL'
    Query = "select * from __instanceModificationEvent within 5 where targetInstance isa 'win32_Service'"
}
$filterResult = Set-WmiInstance @wmiParams
```
Instead of saving a path, save the actual object which will be used for the Binding at the end of this section. Notice that I have a hash table within my splatting hash table to handle all of the arguments that will be applied to the creation of the instance. 
#### Consumer
```
$wmiParams.Class = 'LogFileEventConsumer'
$wmiParams.Arguments = @{
    Name = 'ServiceConsumer'
    Text = 'A change has occurred on the service: %TargetInstance.DisplayName%'
    FileName = "C:\Scripts\Log.log"
}
$consumerResult = Set-WmiInstance @wmiParams
```
The only things that really changed with my WMI hash table is the Class and Arguments which is easily overwritten by adding new things.
#### Binding
```
$wmiParams.Class = '__FilterToConsumerBinding'
$wmiParams.Arguments = @{
    Filter = $filterResult
    Consumer = $consumerResult
}
$bindingResult = Set-WmiInstance @wmiParams
```
#### Removing WMI Subscriptions
Using Get-WMIObject to locate the instance and piping into Remove-WMIObject, you can easily remove one or all of the created WMI instances.  Depending on your objective, you can either Filter for each instance using –Filter or just go crazy and remove everything!
```
##Removing WMI Subscriptions using Remove-WMIObject
#Filter
Get-WMIObject -Namespace root\Subscription -Class __EventFilter -Filter "Name='ServiceFilter'" | 
    Remove-WmiObject -Verbose
 
#Consumer
Get-WMIObject -Namespace root\Subscription -Class LogFileEventConsumer -Filter "Name='ServiceConsumer'" | 
    Remove-WmiObject -Verbose
 
#Binding
Get-WMIObject -Namespace root\Subscription -Class __FilterToConsumerBinding -Filter "__Path LIKE '%ServiceFilter%'"  | 
    Remove-WmiObject -Verbose
```