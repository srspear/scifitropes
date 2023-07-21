
    
import scrapy

class MySpider16(scrapy.Spider):
    name = 'westanispider'
    start_urls = ['https://tvtropes.org/pmwiki/pmwiki.php/Main/ScienceFictionWesternAnimation']
    specific_string = '/WesternAnimation/'

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'FEEDS': {
            'scifiwesternanimation.csv': {'format': 'csv'},
        },
    }

    def parse(self, response):
        a_tags = response.css(f'a[href*="/WesternAnimation/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
