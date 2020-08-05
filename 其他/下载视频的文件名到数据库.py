import os
import pymysql



videoDirNameList = os.listdir('D:\\iwara_dwon\\video')
db =pymysql.connect(
    "127.0.0.1",
    "root",
    "root",
    "compress",
)

def addMysql(sql):
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()


for i in videoDirNameList:
    try:
        sql = "insert into compress_info (dirname) value (%s)" %(i)
        addMysql(sql)
    except:
        print("无法插入，可能已有数据")



db.close()