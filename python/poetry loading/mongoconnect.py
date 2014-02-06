#python requirements
import os

#pymongo requirements
from pymongo import MongoClient

####################################################
####################################################

host = 'localhost'
port = 27017
        
# connect to the mongo instance using connection info
# link to correct database
def makeConnection():   
    global collection
    client = MongoClient(host, port)
    collection = client['gutenberg']['sentences']  

def buildDoc(sentence):
    collection.insert({"file" : sentence[0],
    					"text" : sentence[1],
    					"syl_count" : sentence[2], 
    					"last_word" : sentence[3],
    					"last_syls" : sentence[4],
                       })
