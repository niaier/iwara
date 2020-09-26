# -*- coding: utf-8 -*-
import scrapy
import os
import sys
import io
from scrapy import Selector
from scrapy.http import request
from scrapy.http.cookies import CookieJar
import time
from ..items import IwaraItem
import json
import pymysql
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains   #破解活动验证码的时候用到
from selenium.webdriver.common.by import By   ##按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC  #这个下面的一个是配合来使用的
from selenium.webdriver.support.wait import WebDriverWait  #等待页面加载某些元素
# from ..tools import getDownUrl

surl = 'https://ecchi.iwara.tv/videos/qjz57ce5mbfrgyjkk'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
cookies = {
    'has_js':'1',
    '_ga':'GA1.2.1366874792.1590574696',
    '_gid':'GA1.2.734381663.1590574696',
    'show_adult':'1'

}
class IwaraDownSpider(scrapy.Spider):

    name = 'iwara_down'
    allowed_domains = []#'ecchi.iwara.tv'
    # start_urls = [#'https://ecchi.iwara.tv/videos',
    #               ]
    # def __init__(self):
    #     pass
        # super().__init__()
    #
    def start_requests(self):
        yield scrapy.Request(url=surl, headers=headers,cookies=cookies,callback=self.parse)

    def parse(self, response):

        # download_url = Selector(response=response).xpath('//*[@id="download-options"]/div/ul/li[1]/a/@href').extract()
        download_url = Selector(response=response).xpath('//*[@id="download-options"]/div/ul/li[1]/a/@href').extract()
        author = Selector(response=response).xpath('/html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[1]/div[3]/div[1]/a//text()').extract() #作者名
        categories = Selector(response=response).xpath('/html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[1]/div[3]/div[3]/div//text()').extract()#标签
        made_time = Selector(response=response).xpath('/html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[1]/div[3]/div[1]/text()').extract()#制作日期
        love_view = Selector(response=response).xpath('/html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[1]/div[3]/div[5]//text()').extract()#喜欢和观看
        text = Selector(response=response).xpath('/html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[1]/div[3]/div[2]/div/div//text()').extract()#文本描述

        print(download_url)
        print(author)
        print(categories)
        print(made_time)
        print(love_view)
        print(text)
        #传递下载
        item = IwaraItem()
        src ='https:'+download_url[0]
        title ='test.mp4'
        dirName ='first'
        item['src']=src
        item['title']=title
        item['dirName']=dirName

    # ['//tei.iwara.tv/file.php?expire=1591457386&hash=8686306915685947280159df72aae55ac6b8d6f8&file=2020%2F05%2F27%2F1590572666_QJZ57cE5mBFRGyJKK_Source.mp4&op=dl&r=0']



