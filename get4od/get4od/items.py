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
    
class ProgrammeItem(Item):
    wsprogrammeid = Field()
    series_number = Field()
    archiveepisode = Field()
    episode_number = Field()
    wsprogrammeid = Field() 
    assetid = Field()
    audiodesc_assetid = Field()
    episodeurl = Field()
    requireslogin = Field()
    image_url = Field()
    compliance = Field()
    txtime = Field()
    txday = Field() 
    txdate = Field()
    channellogo = Field() 
    episodeduration = Field()
    episodetitle = Field()
    episodeinfo = Field()
    scrape_error = Field()
    channel = Field()
    link = Field()
    title = Field()
    series_info = Field()
    subtitles = Field()
    audiodesc = Field()
    guidance = Field()
    date = Field()