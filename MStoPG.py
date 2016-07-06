#获取计算资源数据
from pg import DB
import  DBManage

MS=DBManage.DBManage(host="192.168.1.200",port="1433",user="vm",password="password1!",database="VIM_VCDB",charset="UTF-8")
PG = DB(dbname='VM', host='localhost' ,port=5432,user='van',passwd='123456')
MS.getMSSConnetion()

#sql1="SELECT [SAMPLE_TIME] ,[STAT_ID]   ,[STAT_NAME]  ,[STAT_GROUP]  ,[STAT_ROLLUP_TYPE]  ,[COUNTER_ID] ,[ENTITY] ,[DEVICE_NAME] ,[DEVICE_TYPE_NAME]   ,[STAT_VALUE] FROM [VIM_VCDB].[dbo].[VPXV_HIST_STAT_DAILY]"
sql="select A.[SAMPLE_TIME],A.[STAT_NAME],B.[STAT_ROLLUP],B.[UNIT],A.[STAT_GROUP],A.[ENTITY],A.[STAT_VALUE] from [VIM_VCDB].[dbo].[VPXV_HIST_STAT_DAILY] A ,[VIM_VCDB].[dbo].[VPXV_STAT_COUNTERS] B where A.[STAT_ID]=B.[ID] "

cursor1=MS.QuerySql(sql)
Tuple=cursor1.fetchone()
while Tuple:
    PG.insert("vm_state", time=Tuple[0], stat_name=Tuple[1], stat_rollup_type=Tuple[2], unit=Tuple[3], stat_group=Tuple[4],entity=Tuple[5], stat_value=Tuple[6])
    #PG.insert('hist_stat_daily',sample_time=Tuple[0],stat_id=Tuple[1],stat_name=Tuple[2],stat_group=Tuple[3],stat_rollup_type=Tuple[4],counter_id=Tuple[5],entity=Tuple[6],device_name=Tuple[7],device_type_name=Tuple[8],stat_value=Tuple[9])
    Tuple=cursor1.fetchone()

print("成功！")
MS.closeConn()
PG.close()
