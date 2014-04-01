from scrapy.spider import BaseSpider
import datetime

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
    start_urls = (
        'http://www.channel4.com/programmes/4od/catchup/date/%s' % date_url,
        )

    def parse(self, response):
        filename = self.year + '-' + self.month +'-' + self.day +'.html'
        open(filename, 'wb').write(response.body)