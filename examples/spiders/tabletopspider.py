
    
import scrapy

class MySpider10(scrapy.Spider):
    name = 'tabletopspider'
    start_urls = ['https://tvtropes.org/pmwiki/pmwiki.php/Main/ScienceFictionTabletopGames']
    specific_string = '/TabletopGame/'

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'FEEDS': {
            'scifitabletopgames.csv': {'format': 'csv'},
        },
    }

    def parse(self, response):
        a_tags = response.css(f'a[href*="/TabletopGame/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
