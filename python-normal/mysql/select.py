import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "admin", "7654321", "vfc_sptsm", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT id, cardname, cardcode, status, createtime FROM tm_card \
       WHERE id > '%d'" % (1)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        cardname = row[1]
        cardcode = row[2]
        status = row[3]
        createtime = row[4]
        # 打印结果
        print("id=%d,cardname=%s,cardcode=%s,status=%d,createtime=%s" % \
              (id, cardname, cardcode, status, createtime ))
except:
    print("Error: unable to fecth data")

# 关闭数据库连接
db.close()