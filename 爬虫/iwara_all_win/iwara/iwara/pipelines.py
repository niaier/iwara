# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
import scrapy
# class IwaraPipeline(object):

class MyFilesPipeline(FilesPipeline):
    def __init__(self):
        self.headers = {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
        # 指定cookies

        self.cookies = {
            'ga': 'GA1.2.1366874792.1590574696',
            '_gid': 'GA1.2.1729441356.1591439187',
            '_gat': '1'
        }

    def get_media_requests(self, item, info):
        print('在下了0000000000000000')
        yield scrapy.Request(url=item['src'], meta={'item': item})
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        mp4_name = item['title']
        dirName = item['dirName']
        print('正在下载', mp4_name)
        return dirName + '/%s' % (mp4_name)


#https://tei.iwara.tv/file.php?expire=1591472253&hash=07e82697b77018349052813b710cd9201bb0c1d2&file=2020%2F05%2F27%2F1590572666_QJZ57cE5mBFR
#https://tei.iwara.tv/file.php?expire=1591472253&hash=07e82697b77018349052813b710cd9201bb0c1d2&file=2020%2F05%2F27%2F1590572666_QJZ57cE5mBFRGyJKK_Source.mp4&op=dl&r=0