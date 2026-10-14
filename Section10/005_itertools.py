from itertools import combinations,permutations
import sqlite3

str='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

path='Section10/perm001.db'
connection=sqlite3.connect(path)
cursor=connection.cursor()
cursor.execute('create table if not exists tbl001(Password varhcar(12))')



p1=permutations(str,r=11)
for i in p1:
    
    tempStr=""
    for j in i:
        tempStr+=j
    cursor.execute("insert into  tbl001 values(?)",(tempStr,))
    
    connection.commit()
    
    
connection.close()



    

    
    
