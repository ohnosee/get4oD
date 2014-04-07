import datetime
#framework
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
#module
from get4od.items import Get4OdItem, ProgrammeItem

class ScheduleSpider(BaseSpider):
    name = "schedule"
    allowed_domains = ["channel4.com"]
    today = datetime.date.today()
    # allow at least 24 hours to pass before scraping data
    scrapeday = today - datetime.timedelta(days=2)
    year = str(scrapeday.year)
    month = str(scrapeday.month)
    day = str(scrapeday.day)
    date_url = year + '/' + month +'/' + day +'/'
    date_string = year + '-' + month +'-' + day
    start_urls = (
        'http://www.channel4.com/programmes/4od/catchup/date/%s' % date_url,
        )

    def parse(self, response):
        #filename = self.year + '-' + self.month +'-' + self.day +'.html'
        #open(filename, 'wb').write(response.body)
        hxs = HtmlXPathSelector(response)
        items = []
        modules = hxs.select("//div[@class='module cf']")
        for m in modules:
            progs = m.select("ul/li")
            for p in progs:
                if not p.select("@class").extract()[0] == 'unavailable':
                    item = ProgrammeItem()
                    item['wsprogrammeid'] = p.select("@data-wsprogrammeid").extract()[0]
                    item['channel'] = m.select("h2/text()").extract()[0]
                    item['link'] = p.select("a[@class='promo-link']/@href").extract()[0]
                    item['txtime'] = p.select("a[@class='promo-link']/p[@class='txinfo txtime']/text()").extract()[0]
                    item['title'] = p.select("a[@class='promo-link']/p[@class='title']/text()").extract()[0]
                    item['series_info'] = p.select("a[@class='promo-link']/p[@class='series-info']/text()").extract()[0]
                    if p.select("ul[@class='indicators']/li[@class='subtitles']"):
                        item['subtitles'] = "True"
                    else:
                        item['subtitles'] = "False"
                    if p.select("ul[@class='indicators']/li[@class='audiodesc']"):
                        item['audiodesc'] = "True"
                    else:
                        item['audiodesc'] = "False"
                    if p.select("ul[@class='indicators']/li[@class='guidance']"):
                        item['guidance'] = "True"
                    else:
                        item['guidance'] = "False"
                    url = response.url
                    date = '-'.join(num for num in url.split('/')[-4:-1])
                    item['date'] =  date
                    #items.append(item)
                    proglink = 'http://www.channel4.com' + item['link']
                    request = Request(proglink, callback=self.parseprog, dont_filter=True)
                    request.meta['item'] = item
                    yield request
        #yield items
        
    def parseprog(self, response):
        item = response.meta['item']
        wsprogrammeid = item['wsprogrammeid']
        hxs = HtmlXPathSelector(response)
        try:
            data = hxs.select('//li[@data-wsprogrammeid="%s"]' % wsprogrammeid)[0]
            item['series_number'] = data.select("@data-series-number").extract()[0]
            item['archiveepisode'] = data.select("@data-archiveepisode").extract()[0]
            item['episode_number'] = data.select("@data-episode-number").extract()[0]
            item['assetid'] = data.select("@data-assetid").extract()[0]
            item['audiodesc_assetid'] = data.select("@data-audiodesc-assetid").extract()[0]
            item['episodeurl'] = data.select("@data-episodeurl").extract()[0]
            item['requireslogin'] = data.select("@data-requireslogin").extract()[0]
            item['image_url'] = data.select("@data-image-url").extract()[0]
            item['compliance'] = data.select("@data-compliance").extract()[0]
            #item['txtime'] = data.select("@data-txtime").extract()[0]
            item['txday'] = data.select("@data-txday").extract()[0]
            item['txdate'] = data.select("@data-txdate").extract()[0]
            item['channellogo'] = data.select("@data-channellogo").extract()[0]
            item['episodeduration'] = data.select("@data-episodeduration").extract()[0]
            item['episodetitle'] = data.select("@data-episodetitle").extract()[0]
            item['episodeinfo'] = data.select("@data-episodeinfo").extract()[0]
            return item
        except IndexError:
            item['scrape_error'] = "Programme expired"
            return item
        
            
            
        
        