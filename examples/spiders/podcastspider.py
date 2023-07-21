
    
import scrapy

class MySpider7(scrapy.Spider):
    name = 'podcastspider'
    start_urls = ['https://tvtropes.org/pmwiki/pmwiki.php/Main/ScienceFictionPodcasts']
    specific_string = '/Podcast/'

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'FEEDS': {
            'scifipodcasts.csv': {'format': 'csv'},
        },
    }

    def parse(self, response):
        a_tags = response.css(f'a[href*="/Podcast/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
