import pymssql

host = "192.168.1.200"
port = "1433"
user = "vm"
password = "password1!"
database = "VIM_VCDB"
charset = "UTF-8"

conn = pymssql.connect(host="192.168.1.200", port="1433", user="vm", password="password1!", database="VIM_VCDB",
                       charset="UTF-8")
cursor = conn.cursor()
cursor.execute("SELECT * FROM [VIM_VCDB].[dbo].[VPXV_ENTITY] ")
row = cursor.fetchone()

while row:
    for i in row:
        print(i)
    row = cursor.fetchone()
conn.close()
