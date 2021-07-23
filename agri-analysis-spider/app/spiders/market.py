import json

import scrapy


class MofcomSpider(scrapy.Spider):
    name = 'market'
    allowed_domains = ['nc.mofcom.gov.cn']

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
        province["C_LIST"] = cities
        for city in cities:
            yield scrapy.Request("http://nc.mofcom.gov.cn/jghq/marketList", method="POST", headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }, body=f"province={province['P_INDEX']}&city={city['P_INDEX']}&isprod_mark=&par_craft_index=&pageNo=1",
                                 meta={'city': city, 'province': province}, callback=self.parse_market)
        yield province

    def parse_market(self, response):
        province = response.meta['province']
        city = response.meta['city']
        data = json.loads(response.text)
        # print(data)
        if city.get("M_LIST", None) is None:
            city["M_LIST"] = []
        city["M_LIST"].extend(data["result"])
        if data["hasNext"]:
            yield scrapy.Request("http://nc.mofcom.gov.cn/nc/qyncp/province", method="POST", headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }, body=f"province={province['P_INDEX']}&city={city['P_INDEX']}&isprod_mark=&par_craft_index=&pageNo={data['nextPage']}",
                                 meta={'city': city, 'province': province}, callback=self.parse_market)
