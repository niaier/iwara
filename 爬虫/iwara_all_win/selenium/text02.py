import re
import shutil
import os
dirname = '201402280826'
title = 'アダルト動画なら豊富なカテゴリーで楽しめる│アダルト動画投稿シティ｜MMD制作组】液体四溅的背光少女_video.mp4'
old_path = 'E:\\iwara_dwon\\tempo'
fileslist = os.listdir(old_path)
for mp4file in fileslist:
    shutil.move('E:\\iwara_dwon\\tempo\\%s' % mp4file, 'E:\\iwara_dwon\\%s\\%s' % (dirname,title))
# url = 'https://ecchi.iwara.tv/videos?language=zh-hans1002Iwara&sort=date&page=1538'
# a= 'dsd\sdac\s\dw420ksss'
# url02 = 'https://ecchi.iwara.tv/videos/v2ddqs5qzbcewjyzq'
#
# finalpage_url ='/videos/45jgzi5bdjcyjezoz1001Swalla%20%28Megamix%29%20%28R18%29%E3%80%90%E7%B4%B3%E5%A3%AB%E5%90%91%E3%81%91%E3%80%91%20%7C%20Iwara?page=1539'
# finalpage_num = int(re.sub(r'.*page=', '', finalpage_url)[0])
# # b = ['111','222','k']
# # p = re.findall(r'\d+[k]*',a)
#
# x = '作成日:2014-02-28 22:53'
# # dd = re.findall(r'\d+',x)
# dirname = ''.join(re.findall(r'\d+',x))
# # p = re.findall(r'\d+-\d+-\d+ \d+:\d+',x)
# # c = ''.join(b)
# print(dirname)
# # print(dd)
# # print( re.sub(r'.*dw','',a))
# # print(p)
# # print(c)