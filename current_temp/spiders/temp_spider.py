import scrapy
from scrapy_splash import SplashRequest


class MySpider(scrapy.Spider):
    name = "temp"
    start_urls = [
        "http://sh.weather.com.cn/"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        sktemp = response.css('p.sk-temp')
        temp = sktemp.css('span::text').get()
        unit = sktemp.css('em::text').get()
        self.log( f'temp is {temp} {unit}' )
        
        yield { "current_temp": f'{temp} {unit}' }