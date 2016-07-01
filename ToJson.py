

import json
import Enity
enity= Enity.Enity()
enities=enity.getEnity()
i=1
j=1
s=0
with open('graph.json', 'wt') as f:
    f.write("{\n\"nodes\":\n[\n")
    for row in enities:
        print(row[4])
        if(row[4]==7 or row[4]==8 or row[4]==16 or row[4]==18):
            img="res/image/disk.png"
        if (row[4] == 0):
            img  = "res/image/vmware.png"
        if (row[4]==1):
            img  ="res/image/host.png"
        if (row[4] ==19 ):
            img ="res/image/Network.png"


        f.write("{\"name\":"+"\""+row[1]+"\","+"\"image\":"+"\""+img+"\""+'}')

        i+=1

        if(i<=len(enities)):
            f.write(",\n")
        else:
            f.write("\n")
    f.write("],\n")
    f.write("\"links\":\n[\n")
    for row in enities:
        if (row[3]== None):
            f.write("{\"source\":" + str(s) + "," + "\"target\":0}")
            s+=1

        else:
            f.write("{\"source\":" + str(s) + "," + "\"target\":" + str(row[3]) + "}")
            s+=1
        j += 1
        if (j <= len(enities)):
            f.write(",")
        f.write("\n")
    f.write("]\n}")


