# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrapycrawlItem(Item):
    # define the fields for your item here like:
    # name = Field()
    partner_title = Field()
    partner_price = Field()
    site = Field()
    partner_url = Field()
