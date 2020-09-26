# -*- coding: utf-8 -*-
import ffmpy
import os
import re
import time

def get_thumbnail_from_video(video_path,dirpath):
    # thumbnail_path = video_path.replace(".mp4", ".jpg")
    thumbnail_path = "D:/iwara_dwon/video/"+dirname+"/"+dirpath + ".jpg"

    ff = ffmpy.FFmpeg(
        inputs={video_path: None},
        outputs={thumbnail_path: ['-ss', '00:00:05.000', '-vframes', '1']}
    )
    ff.run()
    return thumbnail_path

'''
更多Python学习资料以及源码教程资料，可以在群821460695 免费获取
'''

def findJpg(filename):
    for file in filename:
        if ".jpg" in file:
            return 1

# 文件夹列表
videoDirList = os.listdir("D:/iwara_dwon/video/")
# videoDirList = os.listdir("D:/iwara_dwon/test/video")


for dirname in videoDirList:
    # 文件所在路径
    filename = os.listdir("D:/iwara_dwon/video/"+dirname)
    # 找到视频文件名
    # 筛选jpg
    r = findJpg(filename)
    for file in filename:
        if r!=1 and ".mp4" in file:
            filepath = "D:/iwara_dwon/video/"+dirname+"/"+file
            print(filepath)
            try:
                get_thumbnail_from_video(filepath,dirname)
            except:
                print("失败，重复",dirname)



