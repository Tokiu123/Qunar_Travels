# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from itemadapter import ItemAdapter

class QunarPipeline:
    def __init__(self):
        self.client=pymongo.MongoClient('localhost',27017)
        self.db=self.client['clj2']
        self.Qunar_text=self.db['Qunar_text']

    def process_item(self, item, spider):
        adapter=ItemAdapter(item)
        data=adapter.asdict()
        self.Qunar_text.insert_one(data)
        return item