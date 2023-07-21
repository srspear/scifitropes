
    
import scrapy

class MySpider8(scrapy.Spider):
    name = 'radiospider'
    start_urls = ['https://tvtropes.org/pmwiki/pmwiki.php/Main/ScienceFictionRadio']
    specific_string = '/Radio/'

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'FEEDS': {
            'scifiradio.csv': {'format': 'csv'},
        },
    }

    def parse(self, response):
        a_tags = response.css(f'a[href*="/Radio/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
