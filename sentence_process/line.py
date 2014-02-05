from pymongo import MongoClient


class Line:
	def __init__(self, line):
		self.text = line['text']
		self.file = line['file']
		self.last_syls = line['last_syls']
		self.book_info = {}
	
	def book_find(self):
		host = 'localhost'
		port = 27017
		client = MongoClient(host, port)
		db = client['gutenberg']
		
		e_id = db.fulltext.find({"_id": self.file})[0]['e_id']
		self.book_info = db.etext.find({"_id": e_id})[0]