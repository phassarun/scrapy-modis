# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline


class MyFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        url_splited = url.split('/')
        date = url_splited[-2]
        file_name = url_splited[-1]
        return '{}/{}'.format(date, file_name)
