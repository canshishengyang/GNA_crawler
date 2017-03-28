# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.htmlf
from scrapy.pipelines.files import FilesPipeline

class GnaPipeline(object):
    def process_item(self, item, spider):
        
        return item

class DownloadPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        
        return super(DownloadPipeline, self).get_media_requests(item, info)


    def file_downloaded(self, response, request, info):
        return super(DownloadPipeline, self).file_downloaded(response, request, info)