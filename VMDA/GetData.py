#搞出来了host和vm的数据放在frame里面
import psycopg2
import pandas as pd
from pandas import DataFrame
conn = psycopg2.connect("user=postgres host=192.168.1.112 password=123456 dbname=VM")
cursor=conn.cursor()
cursor.execute("select stat_name,entity,stat_group,stat_rollup_type,stat_value from vm_state where entity like 'vm%' or entity like 'host%'")
rows=cursor.fetchall()
conn.close()
Frame=DataFrame(rows,columns=('State_Name','Entity_Name','State_Group','State_Type','State_Value'))
df=Frame.groupby(['State_Name','Entity_Name','State_Group','State_Type'])
frame=DataFrame(columns=['Group','Value'])
for name, group in df:
    for row in group['State_Value']:
        frame.loc[len(frame)] = [name, row]
