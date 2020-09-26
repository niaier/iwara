# -*- coding: utf-8 -*-
import scrapy
import pymysql
from scrapy import Selector
import re
import time


class IwaraSpider(scrapy.Spider):
    name = 'iwara'
    allowed_domains = ['iwara.tv']
    start_urls = ['http://iwara.tv/']

    def __init__(self):
        # 链接数据库
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,  # 是数字不是字符串
            user='root',
            passwd='root',
            db='iwara'
        )
        # 定义游标
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.urls = ['http://ecchi.iwara.tv/videos']
        self.page_num = []
        self.stop_page = input('输入终止页面:')

        super().__init__()
    # 重写start_requests方法
    def start_requests(self):
        # 浏览器用户代理
        # , headers = headers, cookies = cookies,
        for url in self.urls:
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        # print(response.text)
        # '/html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[2]/ul/li[9]/a'
        # '/html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[2]/ul/li[9]/a'
        # '/html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[2]/ul/li[11]/a'
        # '*//ul[contains(@class,"pager")]/li[-1]/a/@href'

        finalpage_url ='https://ecchi.iwara.tv'+ Selector(response=response).xpath(
            '*//ul[contains(@class,"pager")]//li[contains(@class,"pager-last last")]/a/@href').extract()[0]
        finalpage_num =re.sub(r'.*page=','',finalpage_url)
        curpage = Selector(response=response).xpath('*//li[contains(@class,"pager-current")]/text()').extract()[0]
        # curpage = int(curpage)

        a = input('输入开始页数(倒数)：')
        start_page = int(finalpage_num)-int(a)
        start_url = 'https://ecchi.iwara.tv/videos?page='+str(start_page)

        print(
            '最终页面url', finalpage_url, '\n',
            '最终页面Num', finalpage_num, '\n',
            '开始页面',start_page,'\n',
            '当前页', curpage)


        yield scrapy.Request(url=start_url,callback=self.jump_page)


    def jump_page(self,response):
        print(response.url)
        box = Selector(response=response).xpath(
            '//div[contains(@class,"views-column col")]')
        # print(box.extract())
        # 遍历盒子提取信息
        for obj in box:
            love = obj.xpath(
                './/div[contains(@class,"right-icon likes-icon")]//text()').extract()[1]
            love=re.findall(r'\d+', love)[0]
            views = obj.xpath(
                './/div[contains(@class,"left-icon likes-icon")]//text()').extract()[1]
            views = re.findall(r'\d+[k]*',views)
            views = ''.join(views)
            title = obj.xpath(
                './/h3[contains(@class,"title")]//text()').extract()[0]
            producer= obj.xpath(
                './/a[contains(@class,"username")]//text()').extract()[0]
            playurl = obj.xpath(
                './/h3[contains(@class,"title")]//@href').extract()[0]
            # print(love,'\n','长度',len(love),
            #       views, '\n',
            #       title, '\n',
            #       producer,'\n',
            #       playurl,'\n',)

            sql = 'insert into iwara_info(title,love,views,producer,playurl) values(%s,%s,%s,%s,%s);'
            # self.cursor.execute(sql, [title, love, views, producer, playurl])
            # self.conn.commit()
            try:
                self.cursor.execute(sql, [title,love,views,producer,playurl])
                self.conn.commit()
                print('录入地址',playurl,response.url)
            except:
                print('目录重复，不更新',playurl,response.url)
            # 'https://ecchi.iwara.tv'


        finalpage_url =Selector(response=response).xpath(
            '*//ul[contains(@class,"pager")]//li[contains(@class,"pager-last last")]/a/@href').extract()
        if finalpage_url:
            finalpage_url = finalpage_url[0]
            try:
                finalpage_num = int(re.sub(r'.*page=', '',finalpage_url)) + 1
                print('最终页码1', finalpage_num)
            except:
                finalpage_num = int(re.sub(r'.*page=','',response.url))+1
                print('最终页码2', finalpage_num)
        else:
            finalpage_url = response.url
            finalpage_num = int(re.sub(r'.*page=','',finalpage_url))+1
            print('最终页码3',finalpage_num)

        first_url = 'https://ecchi.iwara.tv'+Selector(response=response).xpath(
            '*//ul[contains(@class,"pager")]//li[contains(@class,"pager-first first")]/a/@href').extract()[0]
        print('第一页',first_url)
        # 当前页页码
        curpage = Selector(response=response).xpath('*//li[contains(@class,"pager-current")]/text()').extract()[0]
        cur_url = re.findall(r'.*page=.*',response.url)
        print('finalpage_num',finalpage_num,response.url)
        print('当前倒数页',int(finalpage_num)-int(curpage))
        print('当前页',curpage,cur_url)

        # 记录页面下载时间
        stop_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        stop_list = '当前倒数页面:'+str(int(finalpage_num)-int(curpage)+1)+'当前页:'+curpage+'当前时间:'+str(stop_time)
        with open('./stop_log.txt','a+',encoding='utf-8') as f:
            f.write(stop_list+'\n')

        # 页码
        # hxs = Selector(response=response).xpath('*//li[contains(@class,"pager-current")]/text()').extract()
        hxs = Selector(response=response).xpath('*//ul[contains(@class,"pager")]//@href').extract()

        for i in hxs:
            page_num = re.sub(r'.*page=','',i)
            try:
                int(page_num)
            except:
                page_num = 0
            if int(page_num) == 0 or page_num== '' :
                pass
            elif int(page_num) <= int(self.stop_page):
                break

            elif page_num not in self.page_num and int(page_num) < int(curpage):
                self.page_num.append(page_num)
                s_url = re.findall(r'.*page=',response.url)[0]+str(page_num)
                yield scrapy.Request(url=s_url,callback=self.jump_page)







