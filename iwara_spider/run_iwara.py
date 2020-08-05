 # -*- coding: utf-8 -*
import os
import json
import time
import pymysql
# os.system("cd ../ex_bookdown/exsp/")
# os.system("python run.py")
# os.system("python ../ex_check/excheck/run.py")
# os.system("python ../ex_info/run.py")
from scrapy import cmdline

date = "iwara"+time.strftime("%Y-%m-%d-%H-%M-%S")+'.tar.gz'
def run_iwarainfo():
    os.chdir("/root/iwara_all_linux/iwara_info/iwara_info/iwara_info/spiders")
    cmdline.execute('scrapy crawl iwara'.split())

def run_videodown():
    os.chdir("/root/iwara_all_linux/iwara_down")
    os.system("python viedeo_down.py")


def tar_gz():
    os.chdir("/root/iwara_all_linux")
    os.system('tar -zvcf  %s filedir' %(date))

def cleanfiledir():
    os.chdir("/root/iwara_all_linux/filedir")
    os.system("rm -rf *")
def cleanDownFaile(videoId):
    db =pymysql.connect(
        "127.0.0.1",
        "root",
        "1qaz@WSX",
        "iwara",
    )
    cursor = db.cursor()
    sql = "update iwara_info set isDown=-1 where id=%s" % videoId
    cursor.execute(sql)
    db.commit()
def  countVideo():
    os.chdir("/root/iwara_all_linux/filedir/")
    # os.system('ls -l | grep "^d" | wc -l')
    with os.popen('ls -l | grep "^d" | wc -l', "r") as p:
        r = p.read()
        print("=======已下载的文件数量是========\n",r)
        print("===============================")


run_type = input('请输入运行类型：\n'
                 '1.下载目录\n'
                 '2.下载视频\n'
                 '3.压缩文件\n'
                 '4.清空下载文件夹\n'
                 '5.下载错误清理\n'
                 '6.统计下载文件数目\n'
                 )

if run_type == '1':
    run_iwarainfo()
elif run_type =='2':
    run_videodown()
elif run_type =='3':
    tar_gz()
elif run_type =='4':
    decideDelet = input("确定清空filedir吗\n"
                        '1.清空\n'
                        "2.否\n")
    if decideDelet == '1':
        cleanfiledir()
elif run_type =='5':
    videoId = input("请输入id号：\n")
    cleanDownFaile(videoId)
elif run_type =='6':
    countVideo()
