#coding=utf-8

import pymysql  # 导入 pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",
                     password="root", db="xwjh", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名

sdf = u'阿斯顿撒大'

# sql = "select * from member where nickname = '%s'" % (sdf)
sql = "insert into testTable ( name, content) VALUES  (%s,%s)"
vvv = ""
print(sql+vvv)
try:

    status = cur.execute(sql,("1223","32323"))  # 执行sql语句
    db.commit()
    # results = cur.fetchall()  # 获取查询的所有记录
    # print(status)
    # print("id", "name", "password")
    # 遍历结果
    # for row in results:
    #     id = row[0]
    #     name = row[1]
    #     password = row[2]
    #     print(id, name, password)
except Exception as e:
    raise e
finally:
    db.close()  # 关闭连接
