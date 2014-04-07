from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
 
import settings
 
DeclarativeBase = declarative_base()
 
def db_connect():
    return create_engine('sqlite:///db/get4od.sqlite')
 
def create_prog_table(engine):
    DeclarativeBase.metadata.create_all(engine)
 
class Programme(DeclarativeBase):
	__tablename__ = "programmes"
	id = Column(Integer, primary_key=True)
	wsprogrammeid = Column(String(10))
	series_number = Column(Integer)
	archiveepisode = Column(Boolean)
	episode_number = Column(Integer)
	assetid = Column(Integer)
	audiodesc_assetid = Column(String(10))
	episodeurl = Column(String(200))
	requireslogin = Column(String(10))
	image_url = Column(String(200))
	compliance = Column(String(200))
	txtime = Column(String(10))
	txday = Column(String(10)) 
	txdate = Column(String(10))
	channellogo = Column(String(10)) 
	episodeduration = Column(Integer)
	episodetitle = Column(String(200))
	episodeinfo = Column(String(200))
	scrape_error = Column(String(50))
	channel = Column(String(10))
	link = Column(String(100))
	title = Column(String(100))
	series_info = Column(String(200))
	subtitles = Column(Boolean)
	audiodesc = Column(Boolean)
	guidance = Column(Boolean)
	date = Column(String(10))
