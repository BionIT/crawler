import scrapy
from .constants import POTTERYBARN_URL

class PotteryBarnCrawler(scrapy.Spider):
    name = 'matter'
    start_urls = [POTTERYBARN_URL + 'shop/furniture/console-tables/']

    def parse(self, response):
        PRODUCT_SELECTOR = 'li.product-cell'
        for item in response.css(PRODUCT_SELECTOR):
            source_selector = '.product-name-container a::attr(href)'
            name_selector = '.product-name-container a::text'
            price_selector = 'span.price-amount::text'

            price = item.css(price_selector).extract_first()
            name = item.css(name_selector).extract_first()

            source = item.css(source_selector).extract_first()




