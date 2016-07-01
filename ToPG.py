
import psycopg2
import  Enity

enities=Enity.Enity()
list=enities.getEnity()
conn = psycopg2.connect(database="VM", user="postgres", password="123456", host="127.0.0.1", port="5432")
cursor=conn.cursor()

for row in list:
     cursor.execute("INSERT INTO Enity  values (%s,%s,%s,%s)",(row[0],row[1],row[2],row[3]));

conn.commit()
print "Records created successfully";
conn.close()