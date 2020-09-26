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
def addMysql(sql):
    cursor.execute(sql)
    return cursor.fetchall()

videoDirList = os.listdir('D:\\iwara_dwon\\video\\')
# print(videoDirList)

def findMp4(filename):
    for file in filename:
        if ".mp4" in file:
            return 1
    return 0

# 遍历文件夹列表    
for dirname in videoDirList:
    # 文件名列表
    filename = os.listdir('D:\\iwara_dwon\\video\\'+dirname)
    fullstr = ''.join(filename)
    if ".mp4" not in fullstr:
        print(dirname,"没有视频文件")
        sql ="select dirname,isDown from iwara_info where dirname=%s" %(dirname)
        print("当前视频数据库注册情况",addMysql(sql))
        




print('完成')




