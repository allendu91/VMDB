#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import DBManage
class Enity:
    sql = "SELECT [ID],[NAME] ,[ENTITY_TYPE],[PARENT_ID]  FROM [VIM_VCDB].[dbo].[VPXV_ENTITY]"
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