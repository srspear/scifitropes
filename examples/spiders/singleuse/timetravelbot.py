import scrapy

class timetravelbot(scrapy.Spider):
    name = 'timetravelbot'
    start_urls = ['https://tvtropes.org/pmwiki/pmwiki.php/Main/TimeTravelTropes']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'FEEDS': {
            'timetravel.csv': {'format': 'csv', 'overwrite': False},
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
        a_tags = response.css(f'a[href*="/Theatre/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
        a_tags = response.css(f'a[href*="/Advertising/"]')
        for tag in a_tags:
            yield {
                'Text': tag.css('::text').get(),
                'URL': tag.attrib['href'],
            }
