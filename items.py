# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):

    number = scrapy.Field()
    name = scrapy.Field()
    fans_count = scrapy.Field()
    avg_reading = scrapy.Field()
    title_reading = scrapy.Field()
    WCI = scrapy.Field()








