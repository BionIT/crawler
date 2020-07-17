import scrapy
from spider.models import Item

#crawler for lego
class WebCrawler(scrapy.Spider):
    name = 'webcrawler'
    items = Item.objects.all()
    allurls = []
    for item in items:
        allurls.append(item.source)
    start_urls = allurls

    def parse(self, response):
        parsed = {}
        parsed['source'] = response.request.url
        for span in response.xpath('//span/text()'):
            val = span.extract()
            splits = val.split(".")
            if len(splits) == 2 and len(splits[-1]) == 2:
                parsed['price'] = float(val[1:])
                break
        for desc in response.xpath('//h1/span/text()'):
            if desc is None or desc.extract() == "":
                continue
            parsed['name'] = desc.extract()
            break
        return parsed

