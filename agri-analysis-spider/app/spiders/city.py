import json

import scrapy
import yaml


class MySQLPipeline:
    def __init__(self):
        mysql_config = yaml.load(open('app/config/database.secret.yml'),
                                 Loader=yaml.SafeLoader)['development']['database']

    def process_item(self, item, spider):
        print(item)

    def close_spider(self):
        pass


class MofcomSpider(scrapy.Spider):
    name = 'city'
    allowed_domains = ['nc.mofcom.gov.cn']
    custom_settings = {
        'ITEM_PIPELINES': {
            'app.spiders.city.MySQLPipeline': 300
        }
    }

    def start_requests(self):
        return [
            scrapy.Request("http://nc.mofcom.gov.cn/nc/qyncp/province", method="POST")
        ]

    def parse(self, response, **kwargs):
        data = json.loads(response.text)
        for item in data:
            yield scrapy.Request("http://nc.mofcom.gov.cn/nc/qyncp/province", method="POST", headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }, body="pIndex=" + item["P_INDEX"], meta={'province': item}, callback=self.parse_city)

    def parse_city(self, response):
        province = response.meta["province"]
        cities = [item for item in json.loads(response.text) if item["P_INDEX"] != province["P_INDEX"]]
        province["CITIES"] = cities
        yield province
