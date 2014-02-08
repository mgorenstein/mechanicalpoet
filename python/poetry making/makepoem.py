import random
import line
import poem

import time

#pymongo requirements
from pymongo import MongoClient

####################################################
####################################################

host = 'localhost'
port = 27017
		
# connect to the mongo instance using connection info
# link to correct database
client = MongoClient(host, port)
collection = client['gutenberg']['sentences']  

test = collection.aggregate([				
	{"$group": {"_id": "$last_syls", "count": { "$sum": 1}}},
	{"$match": {"count": { "$gt": 20 }}}
])

test = test['result']


while True:
    x = random.sample(test, 3)

    poemz = poem.Poem()
    for element in x:
        syl = element['_id']
        results = collection.find({"last_syls": syl})
        size = int(results.count())
        line1 = results[random.randrange(0,size,1)]
        line2 = results[random.randrange(0,size,1)]
        while (line1['last_word'] == line2['last_word']):
            line2 = results[random.randrange(0,size,1)]
        line1 = line.Line(line1)
        line1.book_find()
        line2 = line.Line(line2)
        line2.book_find()
        poemz.add([line1, line2])
    
    poemz.print_poem()
    if (raw_input("Keep? (y/n): ") == 'y'):
        poemz.make_html()