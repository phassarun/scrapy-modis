# -*- coding: utf-8 -*-
import os

import scrapy


class ModisSpider(scrapy.Spider):
    name = 'modis'
    start_urls = ['https://e4ftl01.cr.usgs.gov/MOLT/MOD11A1.006/']
    http_user = os.environ.get('MODIS_USERNAME', None)
    http_pass = os.environ.get('MODIS_PASSWORD', None)

    ALLOW_YEARS = ['2018']
    ALLOW_FILES_NAME = ['h27v06', 'h27v07', 'h27v08', 'h28v07', 'h28v08']
    
    def parse(self, response):
        date_folder_urls = self.get_date_folder_urls(response, self.ALLOW_YEARS)
        for date_folder_url in date_folder_urls:
            yield scrapy.Request(date_folder_url, callback=self.parse_file_urls)

    
    def parse_file_urls(self, response):
        file_urls = self.get_files_urls(response, self.ALLOW_FILES_NAME)
        yield {'file_urls': file_urls}


    def get_date_folder_urls(self, response, allow_years):
        allow_year_str = '|'.join(allow_years)
        regex_pattern = r'^((%s)\.\d{2}\.\d{2})' % allow_year_str

        date_folder_name_list = response.css('a::attr(href)').re(regex_pattern)
        folder_filtered_list = list(filter(lambda date_folder_name: '.' in date_folder_name, date_folder_name_list))
        urls = list(map(lambda date_folder: response.urljoin(date_folder), folder_filtered_list))
        return urls


    def get_files_urls(self, response, allow_files_name):
        allow_file_name_str = '|'.join(allow_files_name)
        regex_pattern = r'(\w{7}\.\w{8}\.(%s)\.\d{3}\.\d{13}.hdf$)' % (allow_file_name_str)

        file_name_list = response.css('a::attr(href)').re(regex_pattern)
        file_name_list_filtered = list(filter(lambda file_name:  'hdf' in file_name, file_name_list))
        file_urls = list(map(lambda file_name: response.urljoin(file_name), file_name_list_filtered))
        return file_urls
