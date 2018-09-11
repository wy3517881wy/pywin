# 导入SQLite驱动:
import sqlite3

conn = sqlite3.connect('localDatabase.db')
cursor = conn.cursor()
# cursor.execute(
#                 'create table if not exists records(recordid INTEGER PRIMARY KEY NOT NULL,createtime text,'
#                 'gender char(100),ordernum int(40),expend char(50),operation char(50),output char(50))')
# cursor.execute('select * from record  ')

c1 = "a001"
c2 = "b002"
c3 = "1000031901171209031000438001126744567818"
c4 = "d004"
c5 = "e005"
f5 = "f006"

#cursor.execute("select * from record")

# sqlss = "insert into records (createtime,gender,ordernum,expend,operation,output) values('"+c1+"','"+c2+"','"+c3+"','"+c4+"','"+c5+"','"+f5+"')"
sqlss = "select sum(recordid) from records where ordernum = '"+c3+"'"
cursor.execute(sqlss)
values = cursor.fetchall()
print(values[0][0]==None)
# for row in values:
#     print(row[0])

cursor.close()
conn.commit()
conn.close()
