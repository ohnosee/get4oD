from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
 
import settings
 
DeclarativeBase = declarative_base()
 
def db_connect():
    return create_engine('sqlite:///data.db')
 
def create_prog_table(engine):
    DeclarativeBase.metadata.create_all(engine)
 
class Programme(DeclarativeBase):
	__tablename__ = "programmes"
	id = Column(Integer, primary_key=True)
	wsprogrammeid = Column(String(200))
	series_number = Column(String(200))
	archiveepisode = Column(String(200))
	episode_number = Column(String(200))
	assetid = Column(String(200))
	audiodesc_assetid = Column(String(200))
	episodeurl = Column(String(200))
	requireslogin = Column(String(200))
	image_url = Column(String(200))
	compliance = Column(String(200))
	txtime = Column(String(200))
	txday = Column(String(200)) 
	txdate = Column(String(200))
	channellogo = Column(String(200)) 
	episodeduration = Column(String(200))
	episodetitle = Column(String(200))
	episodeinfo = Column(String(200))
	scrape_error = Column(String(200))
	channel = Column(String(200))
	link = Column(String(200))
	title = Column(String(200))
	series_info = Column(String(200))
	subtitles = Column(String(200))
	audiodesc = Column(String(200))
	guidance = Column(String(200))
	date = Column(String(200))
