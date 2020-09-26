from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains   #破解活动验证码的时候用到
from selenium.webdriver.common.by import By   ##按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC  #这个下面的一个是配合来使用的
from selenium.webdriver.support.wait import WebDriverWait  #等待页面加载某些元素


def getDownUrl():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)  # 弹出浏览器
    browser.get('https://ecchi.iwara.tv/videos/qjz57ce5mbfrgyjkk')  # 打开要访问的页面
    # print(browser.page_source)
    try:
        # download_url = self.browser.find_element_by_xpath('//*[@id="download-options"]/div/ul/li[1]/a').get_attribute('href')
        # element = browser.find_element_by_class_name("r18-continue btn btn-danger")
        element = browser.find_element_by_xpath('//*[@id="r18-warning"]/div/div/a[1]')
        print(element)
        try:
            element.click()
        except:
            print("已跳过")
    except:
        print('没有找到')

    download_url = browser.find_element_by_xpath('//*[@id="download-options"]/div/ul/li[1]/a').get_attribute('href')
    print(download_url)
    browser.close()
    return download_url

print(getDownUrl())