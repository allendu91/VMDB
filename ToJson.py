#-*- coding:UTF-8 -*-
import os
import json
import Enity
import time
from threading import Thread
import threading

imageSwitch = {0: "res/image/vmware.png",
               1: "res/image/host.png",
               7: "res/image/disk.png",
               8: "res/image/disk.png",
               16: "res/image/disk.png",
               18: "res/image/disk.png",
               19: "res/image/host.png",
               14: "res/image/host.png",
               15: "res/image/host.png",
               17: "res/image/host.png"}



FilePath="graph.json"
num=0
Grphjson=""
def tojson():

    global num
    global Grphjson
    while(1):
        E=[]
        enity = Enity.Enity(E)
        enities = enity.getEnity()
        print("enities大小",len(enities))
        i = 1
        j = 1
        source = []
        target = []
        ID = []
        for row in enities:
            source.append(row[0])
            ID.append(row[0])
        #转变索引
        for row in enities:
            if (row[3] == None):
                target.append(0)
            else:
                target.append(row[3])

        for x in range(len(ID)):
            for y in range(len(target)):
                if (ID[x] == source[y]):
                    source[y] = x
                if (ID[x] == target[y]):
                    target[y] = x
        #写入json文件
        with open(FilePath, 'w', encoding="UTF-8") as f:
            #nodes:
            Grphjson += "{\n\"nodes\":\n[\n"
            for row in enities:
                img = "res/image/vmware.png"
                #选择图片
                if row[4] in imageSwitch:
                    typeid = row[4]
                    img = imageSwitch[typeid]


                name = row[1]
                Grphjson+="{\"name\":" + "\"" + str(name) + "\"" + ",\"image\":" + "\"" + img + "\"" + "}"

                i += 1
                if (i <= len(enities)):
                    Grphjson+=",\n"

                else:
                    Grphjson+="\n"

            Grphjson += "],\n"


            #links:
            Grphjson+="\"links\":\n[\n"

            for x in range(len(source)):
                Grphjson+="{\"source\":" + str(source[x]) + "," + "\"target\":" + str(target[x]) + "}"

                j += 1
                if (j <= len(source)):
                    Grphjson+=","

                Grphjson+="\n"

            Grphjson+="]\n}"

            f.write(Grphjson)
            f.close()

            print("写入字节：",len(Grphjson))
            Grphjson = ""
        time.sleep(10)


t = threading.Thread(target=tojson)
t.start()

