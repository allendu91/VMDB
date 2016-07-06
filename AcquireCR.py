from pg import DB
PG=DB(dbname='VM', host='192.168.1.112' ,port=5432,user='van',passwd='123456')
sql="select A.sample_time,A.stat_name,B.stat_rollup,B.unit,A.stat_group,A.entity,A.stat_value from hist_stat_daily A ,stat_counters B where A.stat_id=B.id "
q=PG.query(sql)
rows=q.getresult()
for row in rows:
    PG.insert("vm_state",time=row[0],stat_name=row[1],stat_rollup_type=row[2],unit=row[3],stat_group=row[4],entity=row[5],stat_value=row[6])
print("成功")
PG.close()