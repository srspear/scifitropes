import scrapy
from urllib.parse import urljoin

class SpecFicBot(scrapy.Spider):
    name = 'specficbot'
    start_urls = ['https://tvtropes.org/pmwiki/pmwiki.php/Main/SpeculativeFictionTropes']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'FEEDS': {
            'speculativefiction_tropes.csv': {'format': 'csv', 'overwrite': True},
        },
    }

    def parse(self, response):
        a_tags = response.css('a[href*="/Main/"]')
        for tag in a_tags:
            text = tag.css('::text').get()
            href = tag.attrib['href']
            url_slug = href.split("/Main/",1)[1]
            yield {
                'Text': text,
                'URL Slug': url_slug,
            }

