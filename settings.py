DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 500,
}


PIPELINES = {
    'scraper.pipelines.files.MyFilesPipeline': 100
}

SPIDER_SETTINGS = [
    {
        'endpoint': 'modis',
        'location': 'scraper.spiders.ModisSpider',
        'spider': 'ModisSpider'
    }
]

SCRAPY_SETTINGS = {
    'ITEM_PIPELINES': PIPELINES,
    'DOWNLOADER_MIDDLEWARES': DOWNLOADER_MIDDLEWARES,
    'FILES_STORE': 'exports',
    'BOT_NAME': 'scraper_modis',
    'SPIDER_MODULES': ['scraper.spiders'],
    'NEWSPIDER_MODULE': 'scraper.spiders',
    'ROBOTSTXT_OBEY': True
}