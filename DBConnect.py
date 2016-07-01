#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
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
        if(row[2]=="DATACENTER_FOLDER"or row[2]=="DATACENTER"):
            img="res/image/disk.png"
        if (row[2] == "VM_FOLDER"or row[2]=="VM_FOLDER"):
            img  = "res/image/vmware.png"
        if (row[2] == "HOST_FOLDER"or row[2]=="CLUSTER_COMPUTE_RESOURCE"or row[2]=="RESOURCE POOL"):
            img  ="res/image/host.png"
        if (row[2] == "NETWORK"or row[2]=="DVSWITCH"or row[2]=="DVPORTGROUP"):
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