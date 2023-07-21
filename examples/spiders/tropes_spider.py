import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import CloseSpider


class TropesSpider(scrapy.Spider):
    name = "tropes"

    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    }

    def start_requests(self):
        try:
            df = pd.read_csv('/home/simeon/Documents/futuretropes2/scifitropes/scifiwesternanimation.csv')
        except pd.errors.EmptyDataError:
            raise CloseSpider('EmptyDataError: The CSV file is empty or not found.')
        except Exception as e:
            raise CloseSpider(f'Error: {e}')

        urls = df['URL'].tolist()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        if response.status != 200:
            self.log(f'Error: {response.url} does not exist or is unavailable.')
            return

        main_article_div = response.css('div#main-article')
        li_tags = main_article_div.css('li')

        tropes = {}
        for li in li_tags:
            a_tag = li.css('a')
            href = a_tag.attrib.get('href')
            if href and '/Main/' in href:
                trope_name = a_tag.css('::text').get()
                if trope_name:
                    tropes[trope_name] = response.urljoin(href)
            else:
                self.log(f'Error: No valid href found in {response.url}')

        yield {'URL': response.url, 'Tropes': tropes, 'Tropes Count': len(tropes)}


# the script will run the Spider
process = CrawlerProcess(settings={
    "FEEDS": {
        "items.csv": {"format": "csv"},
    },
})

try:
    process.crawl(TropesSpider)
    process.start()
except Exception as e:
    print(f'Error: {e}')

