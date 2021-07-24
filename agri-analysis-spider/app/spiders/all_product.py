import json

import scrapy
import requests


class MofcomSpider(scrapy.Spider):
    name = 'all_product'
    allowed_domains = ['nc.mofcom.gov.cn']

    def __init__(self, end=None, **kwargs):
        super().__init__(**kwargs)
        self.end_date = end

    def start_requests(self):
        print("截止日期：", self.end_date)
        res = requests.post(url="http://nc.mofcom.gov.cn/jghq/priceList",
                            data=f"queryDateType=4&timeRange=2021-05-24+~+{self.end_date}",
                            headers={
                                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                            })
        page_count = json.loads(res.content)['totalPageCount']

        return [
            scrapy.Request("http://nc.mofcom.gov.cn/jghq/priceList", method="POST",
                           body=f"queryDateType=4&timeRange=2021-05-24+~+{self.end_date}&pageNo=" + str(page),
                           headers={
                               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                           })
            for page in range(1, page_count + 1)
        ]

    def parse(self, response, **kwargs):
        data = json.loads(response.text)
        for item in data["result"]:
            yield item
