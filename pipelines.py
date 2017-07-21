# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrap_hypedc import settings
import psycopg2

class ScrapHypedcPipeline(object):
     def __init__(self):
         print
         
     def process_item(self, item, spider):
         databaseName = settings.databaseName
         databasePassword = settings.databasePwd
         databaseUser = settings.databaseUser
         databaseHost = settings.databaseHost
         databaseTable = settings.databaseTable
         #conn_string = "dbname='%s' psd='%s' user='%s' host='%s'" % 
         conn_string = "dbname='%s' user='%s' password='%s' host='%s'" % (databaseName, databaseUser, databasePassword, databaseHost)
         self.conn = psycopg2.connect(conn_string)
         self.cur = self.conn.cursor()
         keys = item.keys()
         data = [item[k] for k in keys] # make a list of each key
         instr = 'INSERT INTO {table} ({keys}) VALUES ({placeholders});'.format( 
         table = databaseTable, 
         keys = ", ".join(keys), #iterate through keys, seperated by comma
         placeholders = ", ".join("'"+d+"'" for d in data) 
         )
           
         self.cur.execute(instr, data) # Combine the instructions and data
         self.conn.commit()
         return item
