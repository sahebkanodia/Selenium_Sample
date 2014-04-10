# Scrapy settings for ScrapyCrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'ScrapyCrawl'

SPIDER_MODULES = ['ScrapyCrawl.spiders']
NEWSPIDER_MODULE = 'ScrapyCrawl.spiders'

ITEM_PIPELINES = [
    'ScrapyCrawl.pipelines.JsonWriterPipeline',
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ScrapyCrawl (+http://www.yourdomain.com)'
