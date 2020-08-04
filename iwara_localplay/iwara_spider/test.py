import pymysql
a='1'

db =pymysql.connect(
        "127.0.0.1",
        "root",
        "root",
        "iwara",
)
cursor = db.cursor()
sql = "update iwara_info set isDown=-1 where id=1" 
print(sql)
cursor.execute(sql)
db.commit()
print(results)
