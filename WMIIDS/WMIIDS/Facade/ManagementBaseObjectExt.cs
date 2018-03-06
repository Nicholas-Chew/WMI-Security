using System.Management;

namespace WMIIDS.Facade
{
    public static class ManagementBaseObjectExt
    {
        public static string AllPropertyToString(this ManagementBaseObject mbo)
        {
            var str = string.Empty;
            foreach (PropertyData prop in mbo.Properties)
            {
                str += string.Format("{0}: {1}\n", prop.Name, prop.Value);
            }

            return str;
        }
    }
}
