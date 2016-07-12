#搞出来了host和vm的数据放在frame里面
import psycopg2
import pandas as pd
from pandas import DataFrame
conn = psycopg2.connect("user=postgres host=192.168.1.66 password=123456 dbname=VM")
cursor=conn.cursor()
cursor.execute("select stat_name,stat_group,stat_rollup_type,stat_value from vm_state where entity like 'vm%' and stat_group like 'cpu'")
rows=cursor.fetchall()
conn.close()
Frame=DataFrame(rows,columns=('State_Name','State_Group','State_Type','State_Value'))
Mydict={}
for x in range(len(Frame)):
    currentName = Frame.iloc[x,0]
    currentValue=Frame.iloc[x,3]
    Mydict.setdefault(currentName,[])
    Mydict[currentName].append(currentValue)
VM_CPU=DataFrame.from_dict(Mydict,orient='index').transpose()
