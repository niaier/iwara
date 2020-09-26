from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver import ActionChains   #破解活动验证码的时候用到
from selenium.webdriver.common.by import By   ##按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC  #这个下面的一个是配合来使用的
from selenium.webdriver.support.wait import WebDriverWait  #等待页面加载某些元素
from threading import Thread
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pymysql
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import os
import time
import pyautogui
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



chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(options=chrome_options)  # 弹出浏览器
browser.get(
    # 'https://ecchi.iwara.tv/videos/qjz57ce5mbfrgyjkk'
    # 'https://ecchi.iwara.tv/videos/JoEJiGHlEYWMQ'
    'https://ecchi.iwara.tv/videos/zr2KU3HDVE7bE'
)  # 打开要访问的页面

# browser.get('www.baidu.com')  # 打开要访问的页面

# print(browser.page_source)

# /跳过验证
try:
    # element = browser.find_element_by_class_name("r18-continue btn btn-danger")
    element = browser.find_element_by_class_name("r18-continue.btn.btn-danger")
    # element = browser.find_element_by_xpath('//*[@id="r18-warning"]/div/div/a[1]')
    browser.execute_script(
        "arguments[0].setAttribute('style', arguments[1]);",
        element,
        "border: 2px solid yellow;"  # 边框border:2px; red红色
    )
    print(element)
    try:
        element.send_keys(Keys.ENTER)
    except:
        print("已跳过")
except:
    print('没有找到')


# 下载2
# 找到播放器
def download2(playurl):
    # 定位播放器
    element_player = browser.find_element_by_xpath(
        '//div[contains(@class,"player")]/iframe')
    player_url = element_player.get_attribute('src')
    # 定位点击播放按钮
    browser.get(player_url)
    wait = WebDriverWait(browser,30)
    locator01 =(
        By.XPATH,'/html/body/div[3]/div[2]/div[4]/div[3]/div/div[2]/div[2]/img'
    )
    wait.until(EC.presence_of_element_located(locator01))
    time.sleep(5)
    ActionChains(browser).move_by_offset(250, 250).click().perform()
    locator02 =(
        By.XPATH,'//*[@id="drive-viewer-video-player-object-0"]'
    )
    wait.until(EC.presence_of_element_located(locator02))
    time.sleep(10)
    # ！！！不用xpath定位！！
    # 切换iframe
    iframe = browser.find_elements_by_css_selector('iframe')
    print(iframe[0].get_attribute('id'),'\n',
          )
    # browser.switch_to.default_content()
    browser.switch_to.frame(iframe[0])
    # 获取下载源
    locator03 =(
        By.XPATH,'//video[contains(@class,"html5-main-video")]'
    )
    wait.until(EC.presence_of_element_located(locator03))
    time.sleep(5)
    down_src = browser.find_element_by_xpath(
        '//*[contains(@class,"html5-main-video")]'
    ).get_attribute('src')
    print(down_src)
    browser.get(down_src)
    time.sleep(10)
    # 右键另存视频
    action = ActionChains(browser)
    action.move_by_offset(250, 250).context_click().perform()
    pyautogui.typewrite(
        ['down','down','down','down','enter','enter'])
    sleep(2)
    pyautogui.typewrite(['enter'])

download2('')