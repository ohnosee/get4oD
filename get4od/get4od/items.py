# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Get4OdItem(Item):
    # define the fields for your item here like:
    wsprogrammeid = Field()
    channel = Field()
    link = Field()
    txtime = Field()
    title = Field()
    series_info = Field()
    subtitles = Field()
    audiodesc = Field()
    guidance = Field()
    date = Field()
    
