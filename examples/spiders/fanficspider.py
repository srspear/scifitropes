
    
import scrapy

class MySpider4(scrapy.Spider):
    name = 'fanficspider'
    start_urls = ['https://tvtropes.org/pmwiki/pmwiki.php/Main/ScienceFictionFanFic']
    specific_string = '/FanFic/'

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'FEEDS': {
            'scififanfic.csv': {'format': 'csv'},
        },
    }

    def parse(self, response):
        a_tags = response.css(f'a[href*="/FanFic/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
