#获取实体的类
import DBManage
class Enity:
    sql = "SELECT [ID],[NAME] ,[ENTITY_TYPE],[PARENT_ID],[TYPE_ID]  FROM [VIM_VCDB].[dbo].[VPXV_ENTITY] order by id "
    enities=[]
    def __init__(self,enities):
        self.enities=enities
        db=DBManage.DBManage(host="192.168.1.200",port="1433",user="vm",password="password1!",database="VIM_VCDB",charset="UTF-8")
        db.getMssConnetion()
        self.cursor=db.QuerySql(self.sql)
        row=self.cursor.fetchone()
        while row:
          self.enities.append(row)
          row = self.cursor.fetchone()
        db.closeConn()
    def getEnity(self):
        return self.enities
