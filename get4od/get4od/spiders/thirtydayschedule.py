import datetime
#framework
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
#module
from get4od.items import Get4OdItem

class ScheduleSpider(BaseSpider):
    name = "schedule_date"
    
    def __init__(self):
        today = datetime.date.today()
        delta = datetime.timedelta(days=1)
        allowed_domains = ["channel4.com"]
        # allow at least 24 hours to pass before scraping data
        base_url = 'http://www.channel4.com/programmes/4od/catchup/date/'
        self.start_urls = []
        while delta < datetime.timedelta(days=31):
            scrapeday = today - delta
            year = str(scrapeday.year)
            month = str(scrapeday.month)
            day = str(scrapeday.day)
            date_url = year + '/' + month +'/' + day +'/'
            self.start_urls.append(base_url+date_url)
            delta = delta + datetime.timedelta(days=1)
    
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
                    item = Get4OdItem()
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
                    items.append(item)
        return items