# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QunarItem(scrapy.Item):
    Title = scrapy.Field() # Title：文章标题
    Comment = scrapy.Field()# Comment：作者名称
    TravelLink = scrapy.Field()# TravelLink：标题的链接
    Date = scrapy.Field()# Date：出发日期
    Days = scrapy.Field() # Days：旅游共几天
    Photo_Nums = scrapy.Field()# Photo_Nums：照片数量
    Fee = scrapy.Field()# Fee：人均消费
    People = scrapy.Field()# People：适合人数
    Places = scrapy.Field()# Places：途径地点
    Views = scrapy.Field()# Views：评论人数
    Love = scrapy.Field() # Love：点赞数
    pass
