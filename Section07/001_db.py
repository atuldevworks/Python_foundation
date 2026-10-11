from sqlite3 import connect
dbPath='Section07/db0002.db'

conn=connect(database=dbPath)
cur=conn.cursor()
cur.execute("create table  if not exists tbl002   (name varchar ,roll int)")
cur.execute("insert into tbl002 values(?,?)",("TEST",3))
conn.commit()
conn.close()



conn=connect(database=dbPath)
cur=conn.cursor()

cur.execute("select name,* from  tbl002")
data=cur.fetchall()
conn.close()


print(data)
