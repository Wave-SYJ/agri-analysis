import json

import scrapy


class MofcomSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['nc.mofcom.gov.cn']

    def start_requests(self):
        return [
            scrapy.Request("http://nc.mofcom.gov.cn/jghq/priceList", method="POST",
                           body="queryDateType=4&timeRange=2021-07-23+~+2021-07-23&pageNo=" + str(page),
                           headers={
                               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                           })
            for page in range(1, 507)
        ]

    def parse(self, response, **kwargs):
        data = json.loads(response.text)
        for item in data["result"]:
            yield item
