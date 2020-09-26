from selenium import webdriver
import os
import time
import re
from time import sleep
import json
from time import sleep
from threading import Thread
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pymysql
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import requests
from requests.cookies import RequestsCookieJar
from os.path import join, getsize
import pyautogui


def linkStr(dirName):  # 拼接字符串
    fileName = os.listdir('E:/iwara_dwon/' + dirName)
    fileName = ''.join(fileName)
    print(fileName)
    return fileName


def getdirsize(dirName):
    path = 'E:/iwara_dwon/' + dirName
    size = 0
    for root, dirs, files in os.walk(path):
        size += sum([getsize(join(root, name)) for name in files])
    return size


class DownIwara:
    def __init__(self):
        #获取基本信息
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
        self.down_num = int(input('输入下载的数目:'))
        sql = 'SELECT * FROM iwara_info WHERE love > 100 AND (isDown IS NULL OR isDown="")'
        self.cursor.execute(sql)
        self.ret = self.cursor.fetchmany(self.down_num)
        print(self.ret)

        # super().__init__()
    def config(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.options)
        self.prefs = {'profile.default_content_settings.popups': 0,
                      'download.default_directory': 'E:/iwara_dwon/%s' % 'test111'}
        self.options.add_experimental_option('prefs', self.prefs)

    def loadPage(self,playurl):
        # self.chrome_options = Options()
        # prefs = {'profile.default_content_settings.popups': 0,
        #          'download.default_directory': 'E:\\iwara_dwon\\%s' % 'dirname'}
        # chrome_options.add_experimental_option('prefs', prefs)
        # global driver
        # self.driver = webdriver.Chrome(options=chrome_options)
        driver = self.driver
        driver.get(playurl)
        #跳过r18验证
        # //*[@id="r18-warning"]/div/div/a[1]
        #
        try:
            element_r18 = driver.find_element_by_xpath(
                '//*[@id="r18-warning"]/div/div/a[1]'
            )
            # element_r18 = WebDriverWait(self.driver,10).until(
            #     EC.presence_of_element_located((By.XPATH,'//*[@id="r18-warning"]/div/div/a[1]'))
            # )

            driver.execute_script(
                "arguments[0].setAttribute('style', arguments[1]);",
                element_r18,
                "border: 2px solid yellow;"  # 边框border:2px; red红色
            )
            # ActionChains(self.driver).move_to_element(element_r18).move_by_offset(-5, 5).click().perform()
            try:
                element_r18.send_keys(Keys.ENTER)
            except:
                print('pppppp')


        except:
            print('没有找到')

        #显示隐藏描述
        # /html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[1]/div[3]/div[2]/div/div/a
        try:
            element_showall = driver.find_element_by_xpath(
                '//a[contains(@class,"show")]')
            try:
                element_showall.click()
            except:
                print('点击无效')

        except:
            print('找不到元素showall')

        title = driver.find_element_by_xpath(
            # '//*[@id="node-23408"]/div[1]/div[2]/div[1]/h1'
            '//h1[contains(@class,"title")]').get_attribute('textContent')  # 标题
        producer = driver.find_element_by_xpath(
            '//a[contains(@class,"username")]').get_attribute('textContent')  # 作者名
        categories = driver.find_element_by_xpath(
            '//div[contains(@class,"field-item even")]/a').get_attribute('textContent').split()  # 标签
        made_time = driver.find_element_by_xpath(
            '//div[contains(@class,"submitted")]').get_attribute('textContent').split()
        upload_time = made_time[-2] + ' ' + made_time[-1]  # 制作日期
        love_view = driver.find_element_by_xpath(
            '//div[contains(@class,"node-views")]').get_attribute(
            'textContent').split()  # 喜欢和观看
        description = driver.find_element_by_xpath(
            '//div[contains(@class,"field field-name-body field-type-text-with-summary")]').get_attribute(
            'textContent')  # 文本描述
        # 详细信息表
        self.dirname = ''.join(re.findall(r'\d+',upload_time))
        info_dict= {
            'dirname':self.dirname,
            'title': title,
            'producer': producer,
            'categories': categories,
            'upload_time': upload_time,
            'love_view': love_view,
            'description': description
        }
        json_list = json.dumps(info_dict)

        try:
            os.mkdir('E:/iwara_dwon/' + self.dirname)
        except:
            print('文件夹已存在')
        with open('E:/iwara_dwon/' + self.dirname+'/info.json', 'w') as f:
            f.write(json_list)

        print(title, '\n',
              producer, '\n',
              categories, '\n',
              made_time, '\n',
              love_view, '\n',
              description, '\n')
        print(info_dict)
        return info_dict


    # 下载视频
    def download(self,dirname):

        #获取下载地址！！！！

        try:
            self.prefs = {'profile.default_content_settings.popups': 0,
                     'download.default_directory': 'E:/iwara_dwon/%s' % dirname}
            self.options.add_experimental_option('prefs', self.prefs)
            download_url = self.driver.find_element_by_xpath(
                '//*[@id="download-options"]/div/ul/li[1]/a').get_attribute('href')
            print(download_url,'使用下载1')
            self.driver.get(download_url)
            fileName = linkStr(dirName=dirname)
            while 'crdownload' in fileName:
                print('正在下载中', fileName)
                time.sleep(3)
                fileName = linkStr(dirName=dirname)
                if 'crdownload' not in fileName:
                    fileName = linkStr(dirName=dirname)
                    print(fileName, '下载完成')
                    sql_success = 'UPDATE iwara_info SET isDown=1 WHERE id= %s'
                    self.cursor.execute(sql_success, [id])
                    self.conn.commit()
                    return 1

        except:
            print('下载1无法使用')
            try:
                print('使用下载2')
                self.download2(dirname)
                while True:
                    dirsize =getdirsize(dirName=dirname)
                    time.sleep(5)
                    dirsize02 =getdirsize(dirName=dirname)
                    if dirsize == dirsize02 and dirsize02>=1000:
                        print('下载2完成')
                        break
                sql_success = 'UPDATE iwara_info SET isDown=1 WHERE id= %s'
                self.cursor.execute(sql_success,[id])
                self.conn.commit()
                return 1
            except:
                print('下载无法使用')
                sql_down1fail = 'UPDATE iwara_info SET isDown=-1 WHERE id= %s'
                self.cursor.execute(sql_down1fail,[id])
                self.conn.commit()
                return 0


        # dirName = dirname




    def download2(self,dirname):
        # 定位播放器
        self.prefs = {'profile.default_content_settings.popups': 0,
                      'download.default_directory': 'E:/iwara_dwon/%s' % dirname}
        self.options.add_experimental_option('prefs', self.prefs)
        driver = self.driver
        element_player = self.driver.find_element_by_xpath(
            '//div[contains(@class,"player")]/iframe')
        player_url = element_player.get_attribute('src')
        # 定位点击播放按钮
        driver.get(player_url)
        wait = WebDriverWait(driver, 30)
        locator01 = (
            By.XPATH, '/html/body/div[3]/div[2]/div[4]/div[3]/div/div[2]/div[2]/img'
        )
        wait.until(EC.presence_of_element_located(locator01))
        time.sleep(5)
        ActionChains(driver).move_by_offset(250, 250).click().perform()
        locator02 = (
            By.XPATH, '//*[@id="drive-viewer-video-player-object-0"]'
        )
        wait.until(EC.presence_of_element_located(locator02))
        time.sleep(10)
        # ！！！不用xpath定位！！
        # 切换iframe
        iframe = driver.find_elements_by_css_selector('iframe')
        print(iframe[0].get_attribute('id'), '\n',
              )
        # browser.switch_to.default_content()
        driver.switch_to.frame(iframe[0])
        # 获取下载源
        locator03 = (
            By.XPATH, '//video[contains(@class,"html5-main-video")]'
        )
        wait.until(EC.presence_of_element_located(locator03))
        time.sleep(5)
        down_src = driver.find_element_by_xpath(
            '//*[contains(@class,"html5-main-video")]'
        ).get_attribute('src')
        print(down_src)
        driver.get(down_src)
        time.sleep(10)
        # content = driver.page_source.encode("utf-8")
        driver.get(down_src)

        # cookie
        cookies = driver.get_cookies()  # 定义一个变量，注意这里的get_cookies用法
        print(cookies)
        # 向cookie的name 和value中添加会话信息
        # driver.add_cookie({'name': 'key-solo', 'value': 'value-solo'})

        # 遍历cookies中的name 和value信息并打印，当然还有上面添加的信息
        # for cookie in driver.get_cookies():
        #     print("%s -> %s" % (cookie['name'], cookie['value']))
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }

        jsonCookies = json.dumps(cookies)
        with open('iwaracookie.json', 'w') as f:
            f.write(jsonCookies)
        # 这里我们使用cookie对象进行处理
        jar = RequestsCookieJar()
        with open("iwaracookie.json", "r") as fp:
            cookies = json.load(fp)
            for cookie in cookies:
                jar.set(cookie['name'], cookie['value'])
        driver.close()
        r=requests.get(url=down_src, headers=headers,cookies=jar)
        path = 'E:/iwara_dwon/'+dirname+'/'+title+'.mp4'
        print(path)
        with open(path,'wb') as f:
            f.write(r.content)

d1 = DownIwara()

for cName in d1.ret:
    id = cName['id']
    dirname = cName['dirname']
    playurl = 'https://ecchi.iwara.tv'+cName['playurl']
    title = cName['title']
    producer = cName['producer']
    # categories = cName['categories']
    # upload_time = cName['upload_time']
    # description = cName['description']
    # print(
    #     id,'\n',
    #     dirname,'\n',
    #     playurl,'\n',
    #     title,'\n',
    #     producer,'\n',
    #     categories,'\n',
    #     upload_time,'\n',
    #     description,'\n',
    #       )
    # 配置浏览器
    # d1.config(dirname=dirname)
    # d1.loadPage(playurl=playurl)
    # cd = d1.download()
    # if cd == 1 :
    #     print('下载完成')
    # else:
    #     print(cd)
    d1.config()
    info_dict = d1.loadPage(playurl)
    # categories = ','.join(info_dict['categories'])
    categories = info_dict['categories']
    upload_time = re.findall(r'\d+-\d+-\d+ \d+:\d+',info_dict['upload_time'])[0]+':00'
    description = info_dict['description']
    sql = 'UPDATE iwara_info SET categories=%s,upload_time=%s,description=%s WHERE id=%s;'
    d1.cursor.execute(sql,[categories,upload_time,description,id])
    d1.conn.commit()
    ds = d1.download(info_dict['dirname'])




# with open('iwaracookie.json','r',encoding='utf-8') as f:
#     listCookies=json.loads(f.read())
#     for cookie in listCookies:
#         driver.add_cookie(cookie)1
#     print(listCookies)

# play_url = []





#cookie
# cookies = driver.get_cookies()  # 定义一个变量，注意这里的get_cookies用法
# print(cookies)
# # 向cookie的name 和value中添加会话信息
# driver.add_cookie({'name': 'key-solo', 'value': 'value-solo'})
#
# # 遍历cookies中的name 和value信息并打印，当然还有上面添加的信息
# # for cookie in driver.get_cookies():
# #     print("%s -> %s" % (cookie['name'], cookie['value']))
#
# jsonCookies = json.dumps(cookies)
# with open('iwaracookie.json', 'w') as f:
#     f.write(jsonCookies)


# 读取jsoncookie
# str=''
# with open('iwaracookie.json','r',encoding='utf-8') as f:
#     listCookies=json.loads(f.read())
#     for cookie in listCookies:
#         driver.add_cookie(cookie)
# cookie = [item["name"] + "=" + item["value"] for item in listCookies]
# cookiestr = '; '.join(item for item in cookie)
# print(cookiestr)


# element_show = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[1]/div[4]')
# c2 =element_show.click()
# element_down = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[1]/div[4]/div/div/ul/li[1]')
# c3 = element_show.click()






# driver.quit()

