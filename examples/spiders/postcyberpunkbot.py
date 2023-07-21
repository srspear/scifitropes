import scrapy

class postcyberpunkpot(scrapy.Spider):
    name = 'postcyberpunkbot'
    start_urls = ['https://tvtropes.org/pmwiki/pmwiki.php/Main/PostCyberpunk']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'FEEDS': {
            'postcyberpunk.csv': {'format': 'csv', 'overwrite': False},
        },
    }

    def parse(self, response):
        href_keywords = [
                "/Anime/", "/Animation/", "/ChineseAnimation/", "/WebAnimation/", "/Manga/", "/Manhua/", "/Manhwa/", "/ComicBook/", "/ComicStrip/", "/Literature/", "/Theatre/", "/Art/", "/Myth/", "/AudioPlay/",  "/Podcast/", "/Radio/", "/Music/", "/Advertising/", "/Film/", "/WebOriginal/", "/Webcomic/", "/WebVideo/", "/Blog/", "/Website/", "/LetsPlay/", "/WesternAnimation/", "/VisualNovel/", "/TabletopGame/", "/FanFic/", "/Series/", "/VideoGame/", "/ARG/", "/Toys/", "/Ride/", "/Magazine/"
        ]

        for keyword in href_keywords:
            a_tags = response.css(f'a[href*="{keyword}"]')
            for tag in a_tags:
                yield {
                    'Text': tag.css('::text').get(),
                    'URL': tag.attrib['href'],
                }
    
