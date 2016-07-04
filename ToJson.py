#-*- coding:UTF-8 -*-
import json
import Enity
enity= Enity.Enity()
enities=enity.getEnity()
i=1
j=1
source=[]
target=[]
id=[]
imageSwitch={0:"res/image/vmware.png",
             1:"res/image/host.png",
             7:"res/image/disk.png",
             8:"res/image/disk.png",
             16:"res/image/disk.png",
             18:"res/image/disk.png",
             19:"res/image/host.png",
             14:"res/image/host.png",
             15:"res/image/host.png",
             17:"res/image/host.png"}


for row in enities:
    source.append(row[0])
    id.append(row[0])
for row in enities:
    if(row[3]==None):
        target.append(0)
    else:
        target.append(row[3])

for x in range(len(id)):
    for y in range(len(target)):
        if(id[x]==source[y]):
            source[y]=x
        if(id[x]==target[y]):
            target[y]=x


with open('graph.json', 'wt',encoding="UTF-8") as f:
#nodes:
    f.write("{\n\"nodes\":\n[\n")
    for row in enities:

        img = "res/image/vmware.png"
        if row[4] in imageSwitch:
            typeid=row[4]
            img=imageSwitch[typeid]



        id=row[0]
        name=row[1]
        f.write("{\"name\":"+"\""+str(name)+"\""+",\"image\":"+"\""+img+"\""+"}")

        i+=1

        if(i<=len(enities)):
            f.write(",\n")
        else:
            f.write("\n")
    f.write("],\n")

#links:
    f.write("\"links\":\n[\n")
    for x in range(len(source)):
            f.write("{\"source\":" + str(source[x]) + "," + "\"target\":" + str(target[x]) + "}")
            j += 1
            if (j <= len(source)):
                f.write(",")
            f.write("\n")
    f.write("]\n}")
    f.close()

