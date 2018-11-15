#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 16:37
# @Author  : zero
# @File    : gitHubSpider.py
# @Software: PyCharm

import scrapy

class gitHubSpider(scrapy.Spider):
    name = "gitHub_spider"

    @property
    def start_urls(self):
        start_urls = ["https://github.com/shiyanlou?tab=repositories",
                      'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wNlQyMjoxOTo1N1rOBZKWMA%3D%3D&tab=repositories',
                      'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNVQxMTozMTowNyswODowMM4Bxrsx&tab=repositories',
                      'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMFQxMzowMzo1MiswODowMM4BjkvL&tab=repositories',
                      ]
        return start_urls
    def parse(self, response):
        for github in response.css('li[itemprop="owns"]'):
            yield {
                "name": github.css('a[itemprop="name codeRepository"]::text').re_first(r'\n\s*(.*)'),
                "update_time": github.css('relative-time::attr(datetime)').extract_first()
            }
