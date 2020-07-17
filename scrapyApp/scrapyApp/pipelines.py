# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from spider.models import Item
from scrapy.mail import MailSender

class ScrapyappPipeline:
    def process_item(self, item, spider):
        matched = Item.objects.get(source=item['source'])
        if matched is None:
            print("no matches for source {}".format(item['source']))
            return item
        matched.name = item['name']
        if matched.price > item['price']:
            mailer = MailSender()
            mailer.send(
                to=["yulu.nju@gmail.com"],
                subject="Your {} is on sale now".format(item['name']),
                body="Your {} used to be {}, and now it is {}".format(item['name'], matched.price, item['price']))
        matched.price = item['price']
        matched.save()
        return item
