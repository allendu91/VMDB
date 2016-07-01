
import DBManage
class Enity:
    sql = "SELECT [ID],[NAME] ,[ENTITY_TYPE],[PARENT_ID],[TYPE_ID]  FROM [VIM_VCDB].[dbo].[VPXV_ENTITY] where [TYPE_ID]=0 or [TYPE_ID]=1 or [TYPE_ID]=7 or [TYPE_ID]=8 or [TYPE_ID]=16 or [TYPE_ID]=18 or [TYPE_ID]=19 "
    enities=[]
    def __init__(self):
        db=DBManage.DBManage(host="192.168.1.200",port="1433",user="vm",password="password1!",database="VIM_VCDB",charset="UTF-8")
        db.getConnetion()
        self.cursor=db.QuerySql(self.sql)
        row=self.cursor.fetchone()
        while row:
          self.enities.append(row)
          row = self.cursor.fetchone()
        db.closeConn()
    def getEnity(self):
        return self.enities