import os
import pymysql


db =pymysql.connect(
    "127.0.0.1",
    "root",
    "root",
    "compress",
)
def addMysql(sql):
    cursor.execute(sql)
    db.commit()
# 流程：
# 1读取目录列表【比较下载日期并进行排序】
# 日期有十二位和十四位区别 十二位加00后再比较,加0后还需截掉
# 2每隔50个视频压缩设置压缩密码，命名为从某日期到某日期

# videoDirNameList = os.listdir('D:\\iwara_dwon\\video') #视频文件夹目录

# cursor = db.cursor()
cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
sql = "SELECT * FROM compress_info WHERE isCompress IS NULL OR isCompress<>1"
cursor.execute(sql)
videoDirNameList = cursor.fetchall()

def addMysql(sql):
    cursor.execute(sql)
    db.commit()
# print(videoDirNameList)
# videoDirNameList = []# 添加00的列表
sliceList = []
# listStr = ""
# for item in videoDirNameList:
#     if len(item) == 12:
#         item = item+'00'
#         # print(item)
#         listplus.append(item)
#     elif len(item) ==14:
#         listplus.append(item)

# 列表排序
def takeDirname(elem):
    # print("====================",elem['dirname'])
    return elem['dirname']
videoDirNameList.sort(key=takeDirname,reverse=False)
# 列表分组
for i in range(0,len(videoDirNameList),20):
    a = videoDirNameList[i:i+20]
    sliceList.append(a)
# print(sliceList)

for i,v in enumerate(sliceList):
    print(i,v,"ppppppp")
    # 压缩文件名称
    comppressName = "D:\\iwara_dwon\\视频压缩目录\\"+str(v[0]["dirname"])+"到"+str(v[-1]["dirname"])+".zip"
    listStr=""
    for ind,item in enumerate(v):
        listStr= listStr +" "+ str(item['dirname'])
        dirname = item["dirname"]
        sql = 'update compress_info set isCompress=1 where dirname=%s' %(dirname)
        addMysql(sql)
    # print(comppressName)
    # print(listStr)
    os.chdir("D:\\iwara_dwon\\video")
    # # a = 'tar -zvcf  %s %s' %(comppressName,listStr)
    # # a = 'tar -zvcf  %s %s' %(comppressName,listStr)
    a = 'zip -rP niaier %s %s' %(comppressName,listStr)
    # print("===============a=====================",a)
    os.system(a)




