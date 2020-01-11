import pymysql
# 打开数据库链接
db = pymysql.connect(host="localhost",user="root",password="",db="mysql",port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
sql = "select * from user"
#sql2 = "insert into wp_users(id,user_login,user_pass) values(3,'qq','zjqqqqqq')"
try:
    cur.execute(sql) # 执行sql语句
    results = cur.fetchall() # 获取查询的所有记录
    print("id","name","password")
    # 遍历结果
    for row in results :
        id = row[0]
        name = row[1]
        password = row[2]
        print(id,name,password)
    # cur.execute(sql2)
    # db.commit()


except Exception as e:
    # db.rollback()
    raise e
finally:
    db.close()
