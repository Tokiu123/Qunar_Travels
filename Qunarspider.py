import time#引入time库，降低访问频率
import scrapy#引入爬虫框架scrapy库
from scrapy.selector import Selector#引用Selector方法，对目标response进行解析
from ..items import QunarItem#从父目录中导入QunarItem
class QunarSpider(scrapy.Spider):#编写QunarSpider类
    name = 'Qunarspider'#唯一名字
    # allowed_domains = ['travel.qunar.com']
    start_urls = ['https://travel.qunar.com/travelbook/list.htm?page=1&order=hot_heat']#基地址
    def parse(self, response):
        selector=Selector(response)#对目标返回的response进行解析
        item = QunarItem()#将在items.py定义好的相关字段赋值给变量item
        infos=selector.xpath('//li[starts-with(@class,"list_item")]')#找到循环点，此处为记录每一条游记的标签
        for info in infos:#进行循环
            #经过大量实验可知，某些游记也许存在空值，为了程序的正常运行，则进行抛出异常处理
            try:
                Title = info.xpath('.//h2[@class="tit"]/a/text()').extract()[0]#返回利用xpath已获取Title列表中的第一个元素
                try:
                    TravelLink = info.xpath('.//h2[@class="tit"]/a/@href').extract()[0]#返回利用xpath已获取TravelLink列表中的第一个元素
                except:
                    TravelLink='空'
                try:
                    Date = info.xpath('.//p[@class="user_info"]/span[1]/span[@class="date"]/text()').extract()[0]#返回利用xpath已获取Date列表中的第一个元素
                except:
                    Date="空"
                try:
                    Days = info.xpath('.//p[@class="user_info"]/span[1]/span[@class="days"]/text()').extract()[0]#返回利用xpath已获取Days列表中的第一个元素
                except:
                    Days='空'
                try:
                    Photo_Nums= info.xpath('.//p[@class="user_info"]/span[1]/span[@class="photo_nums"]/text()').extract()[0]#返回利用xpath已获取Photo_Nums列表中的第一个元素
                except:
                    Photo_Nums='空'
                try:
                    Fee = info.xpath('.//p[@class="user_info"]/span[1]/span[@class="fee"]/text()').extract()[0]#返回利用xpath已获取Fee列表中的第一个元素
                except:
                    Fee='空'
                try:
                    People= info.xpath('.//p[@class="user_info"]/span[1]/span[@class="people"]/text()').extract()[0]#返回利用xpath已获取People列表中的第一个元素
                except:
                    People="空"
                try:
                    Places = info.xpath('.//p[@class="places"]/text()').extract()[0]#返回利用xpath已获取Places列表中的第一个元素
                except:
                    Places="空"
                try:
                    Views = info.xpath('.//p[@class="user_info"]/span[2]/span[@class="icon_view"]/span/text()').extract()[0]#返回利用xpath已获取Views列表中的第一个元素
                except:
                    Views="空"
                try:
                    Love= info.xpath('.//p[@class="user_info"]/span[2]/span[@class="icon_love"]/span/text()').extract()[0]#返回利用xpath已获取Love列表中的第一个元素
                except:
                    Love="空"
                try:
                    Comment = info.xpath('.//p[@class="user_info"]/span[1]/span[@class="user_name"]/a/text()').extract()[0]#返回利用xpath已获取Comment列表中的第一个元素
                except:
                    Comment="空"
                item['Title']=Title#赋值
                item['Comment'] = Comment#赋值
                item['TravelLink']=TravelLink#赋值
                item['Date']=Date#赋值
                item['Days']=Days#赋值
                item['Photo_Nums']=Photo_Nums#赋值
                item['Fee']=Fee#赋值
                item['People']=People#赋值
                item['Places']=Places#赋值
                item['Views']=Views#赋值
                item['Love']=Love#赋值
                time.sleep(1)#休息一秒
                yield item#回调item，对items.py中的字段进行赋值
            except IndexError:
                pass
            urls=['https://travel.qunar.com/travelbook/list.htm?page={}&order=hot_heat'.format(str(i))for i in range(2,201)]#对目标网站进行字符串格式化
            for url in urls:#循环
                yield scrapy.Request(url)#利用循环的urlparse回调函数