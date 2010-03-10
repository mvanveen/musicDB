# musicObj.py
# ==============================================================================
# Michael Van Veen
# 03/08/10
# ==============================================================================
# Container classes for song, album, and artist objects
# ==============================================================================
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relation, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Artist(Base):
	__tablename__ = 'artists'

	_id 			= Column(Integer, primary_key=True)
	__name		= Column(String)
	__song		= relation("Song", 	backref=backref('artists', order_by=_id))
	__albums	= relation("Album", backref=backref('artists', order_by=_id))

	def __init__(self, title):
		self.__title = title

	def __repr__(self):
		return("<Artist('%s', '%s')>" % 
			(self.__id, self.__name))

class Album(Base):
	__tablename__ = 'albums'

	_id 			= Column(Integer, primary_key=True)
	__title		= Column(String)
	__song		= relation("Song", backref=backref('albums', order_by=_id))

	def __init__(self, title):
		self.__title = title

	def __repr__(self):
		return("<Album('%s', '%s')>" % 
			(self.__id, self.__title))

class Song(Base): 
	__tablename__ = 'songs'

	_id 				= Column(Integer, primary_key=True)

	__title 		= Column(String)
	__album			= relation(Album, 	order_by=Album._id, backref="songs")
	__artist 		= relation(Artist, 	order_by=Artist._id, backref="songs")
	
	__file_type 	= Column(Integer)
	__file_name		= Column(String)
	__bitrate	 		= Column(Integer)
	__disc_no			= Column(Integer)

	# Song length information
	#length_hr		= Column(Int)
	#length_min	= Column(Int)
	#length_sec	= Column(Int)

	def __init__(self, title, artist, album, fileName,
								disc_no=-1, fileType=-1, bitrate=-1):

		self.__title 			= title
		self.__artist			= artist
		self.__album			= album
		self.__disc_no		= disc_no

		self.__file_type	= fileType
		self.__file_name	= fileName
		self.__bitrate		= fileName #TODO: Ensure kbps is used

	def __repr__(self):
		return("<Song('%s', '%s', '%s', '%s')>" % 
			(self.__id, self.__artist, self.__album, self.__title))

