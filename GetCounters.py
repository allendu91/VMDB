from pg import DB
import  DBManage

MS=DBManage.DBManage(host="192.168.1.200",port="1433",user="vm",password="password1!",database="VIM_VCDB",charset="UTF-8")
PG = DB(dbname='VM', host='localhost' ,port=5432,user='van',passwd='123456')
MS.getMSSConnetion()

sql1="SELECT [ID] ,[STAT_ROLLUP] ,[NAME]  ,[GROUP_NAME]  ,[TYPE]  ,[UNIT]  ,[ASSOCIATE_IDS]   ,[STATS_LEVEL]    ,[FIXED_COLLECTION_INTERVAL]  FROM [VIM_VCDB].[dbo].[VPXV_STAT_COUNTERS]"


cursor1=MS.QuerySql(sql1)
Tuple=cursor1.fetchone()
while Tuple:
    PG.insert('stat_counters',id=Tuple[0],stat_rollup=Tuple[1],name=Tuple[2],group_name=Tuple[3],type=Tuple[4],unit=Tuple[5],associate_ids=Tuple[6],stats_level=Tuple[7],fixed_collection_interval=Tuple[8])
    Tuple=cursor1.fetchone()

print("成功！")
MS.closeConn()
PG.close()
