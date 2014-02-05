import sentence
import mongoconnect
import os, glob
from nltk.tokenize import sent_tokenize

mongoconnect.makeConnection()

os.chdir('/Users/markagorenstein/Documents/Poetry Project/Project Gutenberg/gutenberg_txts/13/')

		 
def run(sentence):
	if (sentence.syl_count == 10):
		sentence.process()
		important = [tFile, sentence.text, sentence.syl_count, sentence.last_word, sentence.last_syls]
		mongoconnect.buildDoc(important)	

for tFile in glob.glob("*.txt"):

	textfile = open(tFile)
	freader = textfile.read()
	sentence_array = sent_tokenize(freader)

	for s in sentence_array:
		try:
			sent = sentence.Sentence(s)
			run(sent)
		except Exception as e:
			print e
			continue