# This is a template for a Python scraper on morph.io (https://morph.io)
import scraperwiki
import lxml.html

html = scraperwiki.scrape("https://majornelson.com/blog/xbox-one-backward-compatibility/")

root = lxml.html.fromstring(html)
i = 1
for tr in root.cssselect("tbody tr"):
    tds = tr.cssselect("td")
    data = {
        'id': i,
        'game': tds[0].text_content(),
        'typ': tds[1].text_content(),
        'publisher': tds[2].text_content(),
        'status': tds[3].text_content(),
    }
    scraperwiki.sqlite.save(unique_keys=['id'], data=data)
    i += 1
    print data
