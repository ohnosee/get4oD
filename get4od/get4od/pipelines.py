# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import Programme, db_connect, create_prog_table
 
class ProgrammePipeline(object):
    def __init__(self):
        engine = db_connect()
        create_prog_table(engine)
        self.Session = sessionmaker(bind=engine)
 
    def process_item(self, item, spider):
        session = self.Session()
        prog = Programme(**item)
        session.add(prog)
        session.commit()
        return item