# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrap_hypedc import settings

class ScrapHypedcPipeline(object):
     def __init__(self):
         import psycopg2
         databaseName = settings.databaseName
         databaseUser = settings.databaseUser
         databaseHost = settings.databaseHost
         self.databaseTable = settings.databaseTable
         conn_string = "dbname='%s' user='%s' host='%s'" % (databaseName, databaseUser, databaseHost)
         self.conn = psycopg2.connect(conn_string)

     def process_item(self, item, spider):
         return item
