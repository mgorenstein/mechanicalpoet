from nltk.tokenize import word_tokenize
from nltk_contrib.readability.textanalyzer import syllables_en
from nltk.corpus import cmudict

class Sentence:
    def __init__(self, sentence):
		self.text = str.join(" ", sentence.splitlines())
		self.words_array = word_tokenize(sentence)
		self.syl_count = 0
		self.last_word = None
		self.last_syls = None
		self.options = None
		self.get_total_syl()

    def process(self):
		self.find_last_word()
		self.get_last_syl(self.last_word)

    def get_total_syl(self):
		for word in self.words_array:
			word_syl = syllables_en.count(word)
			self.syl_count += word_syl
		
    def find_last_word(self):
		for word in reversed(self.words_array):
			if word.isalpha():
				self.last_word = word
				break

    def get_last_syl(self, word):
		breakdown = cmudict.dict()[word][0]
		options = len(breakdown) - 2
		self.last_syls = breakdown[options] + breakdown[options + 1]