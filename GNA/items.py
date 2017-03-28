# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GnaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class PjItem(scrapy.Item):
    pj_name = scrapy.Field()
    pj_desc = scrapy.Field()
    pj_date = scrapy.Field()
    pj_members = scrapy.Field()
class FileItem(scrapy.Item):
    pj_name = scrapy.Field()
    file_urls = scrapy.Field()
    