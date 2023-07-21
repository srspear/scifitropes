import scrapy

class robotrollbot(scrapy.Spider):
    name = 'robotrollbot'
    start_urls = ['https://tvtropes.org/pmwiki/pmwiki.php/Main/RobotRollCall']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'FEEDS': {
            'robotrollcall.csv': {'format': 'csv', 'overwrite': False},
        },
    }

    def parse(self, response):
        a_tags = response.css(f'a[href*="/Main/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/Anime/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/Manga/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/ComicBook/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/Literature/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/Podcast/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/Radio/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/Film/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/WebOriginal/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/Webcomic/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/WesternAnimation/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/VisualNovel/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/TabletopGame/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/FanFic/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/Series/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/VideoGame/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }