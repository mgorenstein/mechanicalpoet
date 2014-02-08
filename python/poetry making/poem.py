import io

class Poem:
	def __init__(self):
		self.poem = []
		self.index = 0
	
	def add(self, line_pair):
		self.poem.append(line_pair[0])
		self.poem.append(line_pair[1])
	
	def print_poem(self):
		for line in self.poem:
			print line.text
	
	def make_html(self):
	
		with open('count.yaml', 'r') as f:
			first_line = f.readline()
			number = int(filter(str.isdigit, first_line)) + 1
			
		html = "---\nlayout: poem\ntitle:" + str(number) + "\n---\n"
		for line in self.poem:
			text = line.text
			title = line.book_info['title']
			author = line.book_info['creator']['full_name']
			if (title == None):
				title = ''
			if (author == None):
				author = 'Unknown'
			blurb = title + ' by ' + author
			html+= "<li><span class='hint--info hint--right' data-hint='" + blurb + "'>" + text + "</span></li>\n"

		with io.open("poems/" + str(number) + ".html", 'a+', encoding='utf-8') as the_file:
			the_file.write(html)
		
		with open('count.yaml', 'w') as f:
			toWrite = 'count: ' + str(number)
			f.write(toWrite)