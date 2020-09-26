# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger

class IwaraInfoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class IwaraInfoDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumMiddleware:
    def __init__(self, timeout=None, service_args=[]):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        # self.browser.set_window_size(1400, 700)
        # self.browser.set_page_load_timeout(self.timeout)
        # self.wait = WebDriverWait(self.browser, self.timeout)

    # def __del__(self):
    #     self.browser.close()

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
    #                service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))
    #
    #
    def process_request(self, request, spider):
        """
         用chrome抓取页面
         :param request: Request对象
         :param spider: Spider对象
         :return: HtmlResponse
        """
        self.browser.get(request.url)
        try:
            # element = browser.find_element_by_class_name("r18-continue btn btn-danger") r18-continue btn btn-danger
            element_r18 = self.browser.find_element_by_xpath(
                # '//a[contains(@class,"r18-continue btn btn-danger)]'
                '//*[@id="r18-warning"]/div/div/a[1]'
            )
            print(element_r18)
            try:
                element_r18.click()
            except:
                print("r18验证已确定")
        except:
            print('r18验证无')

            # /html/body/div[2]/div/div/a[1]
        try:
            element_showall = self.browser.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div[2]/div/div/div/div[1]/div[3]/div[2]/div/div/a')
            print(element_showall)
            try:
                element_showall.click()
            except:
               print("showall已点击")
        except:
            print('showall无')
        response = HtmlResponse(url=self.browser.current_url, body=self.browser.page_source, encoding='utf-8', request=request)
        # self.browser.close()
        return response

    def process_exception(self, request, exception, spider):

        return None


