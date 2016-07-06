#PG数据库操作类
#-*- coding:UTF-8 -*-
import psycopg2
import sys
class PG:

    #获得PostgreSql连接
    def getPGConnection(self):
        try:
            self.conn = psycopg2.connect("user=postgres password=123456 dbname=VM")
            self.cursor = self.conn.cursor()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
    def SaveSql(self,sql):
        self.cursor.execute(sql)
    def QuerySql(self,sql):
        self.cursor.execute(sql)
        return self.cursor
    def closeConn(self):
        self.conn.close()


