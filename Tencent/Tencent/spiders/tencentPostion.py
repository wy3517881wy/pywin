# -*- coding: utf-8 -*-
import scrapy
import pymysql
import Tencent.items

class TencentpostionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']
    url = "http://hr.tencent.com/position.php?&start="
    offset = 0
    # 起始url
    start_urls = [url + str(offset)]

    def parse(self, response):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='xwjh', charset="utf8")
        cur = conn.cursor()

        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            sql = 'INSERT INTO testTable ( name, content, page ,peopleNumber ,workLocation , publishTime) VALUES (%s,%s,%s,%s,%s,%s)'
            # 初始化模型对象
            item = Tencent.items
            # sql = sql + '('+each.xpath("./td[1]/a/text()").extract()[0]+','+each.xpath("./td[1]/a/@href").extract()[0]+','+each.xpath("./td[2]/text()").extract()[0]+','+each.xpath("./td[3]/text()").extract()[0]+','+each.xpath("./td[4]/text()").extract()[0]+','+each.xpath("./td[5]/text()").extract()[0]+' )'
            try:
                print(sql)
                A = cur.execute(sql,(each.xpath("./td[1]/a/text()").extract()[0],each.xpath("./td[1]/a/@href").extract()[0],each.xpath("./td[2]/text()").extract()[0],each.xpath("./td[3]/text()").extract()[0],each.xpath("./td[4]/text()").extract()[0],each.xpath("./td[5]/text()").extract()[0]))
                conn.commit()
                print('成功')
            except:
                print("错误")
            # setattr(item,'positionname',each.xpath("./td[1]/a/text()").extract()[0])
            # 职位名称
            # item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # # 详情连接
            # item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # # 职位类别
            # item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # # 招聘人数
            # item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # # 工作地点
            # item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # # 发布时间
            # item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            # print("positionlink"+item['positionlink'])
            # print("positionType"+item['positionType'])
            # print("peopleNum"+item['peopleNum'])
            yield item

        if self.offset < 1680:
            self.offset += 10

        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
