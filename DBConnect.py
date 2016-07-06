import PGManage

user = "porstgres"
password = "123456"
database = "VM"

PG=PGManage.PG()

PG.getPGConnection()
cursor=PG.QuerySql("select * from enity")
row = cursor.fetchone()
while row:
    for i in row:
        print(i)
    row = cursor.fetchone()
PG.closeConn()
