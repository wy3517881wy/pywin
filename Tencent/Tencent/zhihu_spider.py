import csv

from bs4 import BeautifulSoup
from scrapy import Spider, Selector, FormRequest
from urllib2 import Request
import scrapy


class ZhihuItem(scrapy.Item):
        questionTitle = scrapy.Field()

        url = scrapy.Field()

        follow = scrapy.Field()

        page_view = scrapy.Field()

class ZhihuQuestionSpider(Spider):

        url_base = 'https://www.zhihu.com'  # 供后面获取链接使用

        name = 'login'  # Spider的名字

        start_url_base = 'https://www.zhihu.com/collection/27915947?page='  # 爬取页面

        start_urls = ['https://www.zhihu.com/collection/27915947']  # 这里没用到这个

        headers = {

        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",

        "Accept-Encoding": "gzip,deflate",

        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",

        "Connection": "keep-alive",

        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",

        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36",

        "Referer": "http://www.zhihu.com"

        }

        def start_requests(self):
            return [
            Request("https://www.zhihu.com/", headers=self.headers, meta={"cookiejar": 1}, callback=self.post_login)]

        def post_login(self, response):

            self.log('preparing login...')

            xsrf = Selector(response).xpath('//div[@data-za-module="SignInForm"]//form//input[@name="_xsrf"]/@value').extract()[0]

            self.log(xsrf)

            return FormRequest("https://www.zhihu.com/login/email", meta={'cookiejar': response.meta['cookiejar']},

                headers = self.headers,

                formdata = {

                '_xsrf': xsrf,

                'password': '111111',

                'email': '771331973@qq.com',

                'remember_me': 'true',

            },

                callback=self.after_login,

            )

        # 登陆成功后从start_urls里读出初始url，注入cookie

        def after_login(self, response):

        # 创建csv文件

            with open('items.csv', 'w', newline='') as csvfile:

                writer = csv.writer(csvfile, dialect=('excel'))

            writer.writerow(['标题', '链接', '关注量', '浏览量'])

            for page in range(1, 92):

                url = self.start_url_base + str(page)

            yield Request(url, meta={'cookiejar': 1}, headers=self.headers, callback=self.request_question)

        def request_question(self,request):

            soup = BeautifulSoup(request.body, 'lxml')

            for urlDiv in soup.find_all('div', class_='zm-item'):

                url = self.url_base + urlDiv.find('a').get('href')

            yield Request(url,meta={'cookiejar':1},headers = self.headers,callback=self.parse_question)

        # 获取有用的信息

        def parse_question(self, response):

            soup = BeautifulSoup(response.body, 'lxml')

            item = ZhihuItem()

            item['questionTitle'] = soup.find('h1').string

            item['url'] = response.url

            followDiv = soup.find('div', class_='NumberBoard QuestionFollowStatus-counts')

            item['follow'] = followDiv.find_all('div', class_='NumberBoard-value')[0].string

            item['page_view'] = followDiv.find_all('div', class_='NumberBoard-value')[1].string

        # 将问题标题写入csv

            with open('items.csv', 'a', newline='') as csvfile:

                writer = csv.writer(csvfile, dialect=('excel'))

                writer.writerow([item['questionTitle'], item['url'], item['follow'], item['page_view']])

            return item


