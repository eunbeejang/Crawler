# -*- coding: utf-8 -*-


import scrapy


class BiaslyItem(scrapy.Item):

    title = scrapy.Field()		# Article name
    body = scrapy.Field()		# Article body
    url = scrapy.Field()		# Article url

    pass

# https://www.youtube.com/watch?v=M_vUt-oe1U8
# https://www.youtube.com/watch?v=ivS3FzAL9ss