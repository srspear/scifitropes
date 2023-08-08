import scrapy

class longtropebot(scrapy.Spider):
    name = 'longtropebot'
    start_urls = ['https://tvtropes.org/pmwiki/pmwiki.php/Main/CrapsackWorld', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/AnimeAndManga', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/ComicBooks', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/FanWorks', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/LiveActionFilms', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/Literature', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/LiveActionTV', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/Music', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/MythsAndReligion', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/TabletopGames', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/Theatre', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/VideoGames', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/VisualNovels', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/Webcomics', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/WebOriginal', 'https://tvtropes.org/pmwiki/pmwiki.php/CrapsackWorld/WesternAnimation']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'FEEDS': {
            'crapsackworld.csv': {'format': 'csv'},
        },
    }

    def parse(self, response):
        href_keywords = ["/Anime/", "/Animation/", "/ChineseAnimation/", "/WebAnimation/", "/Manga/", "/Manhua/", "/Manhwa/", "/ComicBook/", "/ComicStrip/", "/Literature/", "/Theatre/", "/Art/", "/Myth/", "/AudioPlay/",  "/Podcast/", "/Radio/", "/Music/", "/Advertising/", "/Film/", "/WebOriginal/", "/Webcomic/", "/WebVideo/", "/Blog/", "/Website/", "/LetsPlay/", "/WesternAnimation/", "/VisualNovel/", "/TabletopGame/", "/FanFic/", "/Series/", "/VideoGame/", "/ARG/", "/Toys/", "/Ride/", "/Magazine/", "/Pinball/", "/Wrestling/", "/Roleplay/"]

        for keyword in href_keywords:
            a_tags = response.css(f'a[href*="{keyword}"]')
            for tag in a_tags:
                yield {
                    'text': tag.css('::text').get(),
                    'url': tag.attrib['href'],
                    'source_url': response.url
                }

