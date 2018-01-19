## Domain Generating Algorithms
C2 server plays an essential role in coordating botnets and malware. Hence, if the malware listens to a static domain it can be take down easily by setting it into a sinkhole.
A Domain Generating Algorithm is a class of algorithm that takes a seed as an input, outputs a string and appends a top level domain (TLD) such as .com, .ru, .uk, etc. in order to form a possible domain name. The seed is a piece of information accessible to both the bot herder and the infected host now acting as a bot.

### Example 
[Dyreza DGA] (https://gist.github.com/jedisct1/33ab6b4e81209dbf53a3)
[Explained: Domain Generating Algorithm] (https://blog.malwarebytes.com/security-world/2016/12/explained-domain-generating-algorithm/)