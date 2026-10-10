from sqlite3 import connect
dbPath='Section07/db0001.db'

conn=connect(database=dbPath)
cur=conn.cursor()
# cur.execute("create table tbl002  (name varchar primary key ,roll int)")
cur.execute("insert into tbl002 values('atul kumar',34)")
conn.commit()
conn.close()
