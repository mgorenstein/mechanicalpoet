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
		html = "---\nlayout: poem\ntitle: 2\n---\n"
		for line in self.poem:
			text = line.text
			title = line.book_info['title']
			author = line.book_info['creator']['full_name']
			print title
			print author
			if (title == None):
				title = ''
			if (author == None):
				author = 'Unknown'
			blurb = title + ' by ' + author
			print blurb
			html+= "<li><span class='hint--info hint--right' data-hint='" + blurb + "'>" + text + "</span></li>\n"
		
		with open('../mechanicalpoet/', 'r') as f:
			first_line = f.readline()
			number = filter(str.isdigit, first_line)

		with io.open("../mechanicalpoet/poems/" + number + ".html", 'w', encoding='utf8') as the_file:
			the_file.write(html)