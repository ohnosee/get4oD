# Scrapy settings for get4od project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'get4od'

SPIDER_MODULES = ['get4od.spiders']
NEWSPIDER_MODULE = 'get4od.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'

EXTENSIONS = {
   'scrapy.telnet.TelnetConsole': None,
   'scrapy.webservice.WebService': None
}