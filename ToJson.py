#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json
import Enity

enity= Enity.Enity()
enities=enity.getEnity()
with open('graph.json', 'wt') as f:
    for row in enities:
        f.write(str(row))