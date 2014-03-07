# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
# 
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
# 
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
# 
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
# 
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.

import requests
import datetime
from bs4 import BeautifulSoup
import scraperwiki

def main():
    index = 0
    scraperwiki.sqlite.execute("drop table if exists swdata")
    '''if scraperwiki.sqlite.get_var('lastindex') == None:
        index = 0
    else:
        index = scraperwiki.sqlite.get_var('lastindex')'''
    dates = builddates()
    for date in dates:
        page = getpage(date)
        progtitles = getProgTitles(page)
        for prog in progtitles:
            index += 1
            #scraperwiki.sqlite.save(unique_keys=['index'], data={"index": index, "year": str(date.year), "month": str(date.month), "day": str(date.day), "link":prog})
            scraperwiki.sqlite.save(unique_keys=['index'], data={"index": index, "year": str(date.year), "month": str(date.month), "day": str(date.day), "prog":prog})
    scraperwiki.sqlite.save_var('lastindex', index)

def builddates():
    today = datetime.date.today()
    i = datetime.timedelta(days=0)
    dates = []
    while i < datetime.timedelta(days=30):
        i = i + datetime.timedelta(days=1)
        dates.append(today - i)
    return dates

def getpage(date):
    baseurl = 'http://www.channel4.com/programmes/4od/catchup/date/'
    url = baseurl+str(date.year)+'/'+str(date.month)+'/'+str(date.day)+'/'
    r = requests.get(url)
    if r.status_code == 200:
        page = r.text
    else:
        page = None
    return page

def getURLS(page):
    soup = BeautifulSoup(page)
    progdata = soup.find_all("a", class_="promo-link")
    progs = []
    for link in progdata:
        href = link.get('href')
        progs.append(href)
    return progs


def getProgTitles(page):
    soup = BeautifulSoup(page)
    progdata = soup.find_all("a", class_="promo-link")
    progs = []
    for prog in progdata:
        progsoup = BeautifulSoup(prog.contents[0])
        progtitle = progsoup.find("p", class_="title")
        progtitle = unicode(progtitle.string)
        progs.append(progtitle)
    return progs

def savepage(page, date):
    filename = str(date.year)+'-'+str(date.month)+'-'+str(date.day)+'.html'
    f = open(filename, 'w')
    f.write(page)
    f.close()

if __name__ == '__main__':
    main()

