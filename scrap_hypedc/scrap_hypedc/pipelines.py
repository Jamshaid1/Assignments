# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrap_hypedc import settings
import psycopg2
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String

class ScrapHypedcPipeline(object):
     con=""
     meta=""
     def __init__(self):
         
         db = settings.databaseName
         password = settings.databasePwd
         user = settings.databaseUser
         host = settings.host
         port = settings.port
 
         # connect with the help of the PostgreSQL URL
         # postgresql://admin:****@localhost:5432/crawl_website
         url = 'postgresql://{}:{}@{}:{}/{}'
         url = url.format(user, password, host, port, db)
         global con
         con = sqlalchemy.create_engine(url, client_encoding='utf8')
         
         # bind the connection to MetaData()
         global meta
         meta = sqlalchemy.MetaData(bind=con, reflect=True)
         con.execute("DROP TABLE IF EXISTS product_info")
         
         #create table product_info
         product_info = Table('product_info',meta,
         Column('product_name', String),
         Column('brand', String),
         Column('color', String),
         Column('currency', String),
         Column('price', String),
         Column('product_url', String)
         )
         meta.create_all(con)
        
    
     def process_item(self, item, spider):
         con.execute(meta.tables['product_info'].insert(),item)
         return item
