
    
import scrapy

class MySpider15(scrapy.Spider):
    name = 'webcomicspider'
    start_urls = ['https://tvtropes.org/pmwiki/pmwiki.php/Main/SciFiWebcomics']
    specific_string = '/Webcomic/'

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'FEEDS': {
            'scifiwebcomics.csv': {'format': 'csv'},
        },
    }

    def parse(self, response):
        a_tags = response.css(f'a[href*="/Webcomic/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
