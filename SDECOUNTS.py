import arcpy
import csv
from arcpy import env
env.workspace = r'C:\Projects\Counties\Grand County UT\LGIM_DB\LGIM.gdb'
fds = arcpy.ListDatasets("","FEATURE")
with open(r'C:\Projects\Counties\Grand County UT\CSV.csv', 'wb') as csvfile:
    wr = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    wr.writerow(["Feature Dataset","Feature Class","Counts"])
    for fd in fds:
##        print fd
        wr.writerow([fd])
        fcs = arcpy.ListFeatureClasses("", "", fd)
        for fc in fcs:
            result = arcpy.GetCount_management(fc)
            count = int(result.getOutput(0))
##            print(fc)
##            print(count)
            wr.writerow(["", fc])
            wr.writerow(["","",count])
del wr
