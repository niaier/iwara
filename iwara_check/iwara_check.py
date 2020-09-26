# -*- coding: utf-8 -*-
import os
import pymysql
import re
import time

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,  # 是数字不是字符串
    user='root',
    passwd='root',
    db='iwara'
)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
videoDirList = os.listdir('D:\\iwara_dwon\\video\\')
# print(videoDirList)

def findMp4(filename):
    for file in filename:
        if ".mp4" in file:
            return 1
    return 0
# 'D:\\iwara_dwon\\test\\'
# 'D:\\iwara_dwon\\video\\'
for dirname in videoDirList:
    filename = os.listdir('D:\\iwara_dwon\\video\\'+dirname)
    a=findMp4(filename)
    for file in filename:
        # print(file)
        if a and ".mp4" in file:
            videoFileName = file
            # print(videoFileName)
            # print(dirname)
            # print(videoFileName)
            videoFileName = re.sub(r"\.mp4$",'',videoFileName)
            # print(videoFileName)
            sql = "UPDATE iwara_info SET isDown=1,title=%s WHERE dirname=%s"
            cursor.execute(sql, [videoFileName,dirname])
            conn.commit()
            # print(dirname)
        elif a==0:
            # print(dirname,"没有mp4")
            break
            # pass


print('完成')




