# get the list of id from links-id-en-pages (id of english wikipedia page)

# output supposed to be files which contains only article within the id (smaller version of the original en-wiki)

# assuming ids = list of sorted english wikipedia id

import re

# directory of en-wiki file
en_wiki_directory = 'enwiki-20170220-pages-articles-multistream.xml'
# directory folder of output folder will be
en_ids_directory = 'en_ids.txt'

output_folder = 'output-en/'

def is_beginning_of_page(line):
	return line == '<page>'

def is_end_of_page(line):
	return line == '</page>'

def get_title_from_line(line):
	m = re.search('<title>(.*)</title>', line)
	return m.group(1)

def get_id_from_line(line):
	m = re.search('<id>(.*)</id>', line)
	return m.group(1)

def get_content_from_text_tag(tag_type, line):
	if tag_type == 'complete':
		m = re.search('^<text xml:space="preserve">(.*)</text>$', line)
	elif tag_type == 'opening':
		m = re.search('^<text xml:space="preserve">(.*)$', line)
	else:
		m = re.search('(.*)</text>$', line)
	if m == None:
		return ''
	return m.group(1)

class Page:

	def __init__(self, page_id, title, content):
		self.page_id = page_id
		self.title = title
		self.content = content

	def print_to_file(self):
		out = open(output_folder + str(self.page_id) + '.txt', 'w')
		out.write(str(self.page_id)+'\n')
		out.write(page.title+'\n')
		out.write(page.content)
		out.close()


f_ids = open(en_ids_directory, 'r')
ids = []

for line in f_ids:
	line = line.strip()
	doc_id = int(line)
	ids.append(doc_id)

f_ids.close()


f = open(en_wiki_directory,'r')

in_page = False
page = None
in_text = False
is_first_id = True
index = 0

for line in f:
	line = line.strip()
	if is_beginning_of_page(line):
		in_page = True
	elif is_end_of_page(line):
		if index == len(ids):
			print "Done"
			exit()
		if ids[index] < page.page_id:
			index += 1
		if page.page_id == ids[index]:
			print "Document id:", page.page_id
			page.print_to_file()
			index += 1
		in_page = False
		page = None
		is_first_id = True
	else:
		if in_page:
			# if this line is the title line
			if "<title>" in line and "</title>" in line:
				title = get_title_from_line(line)
				page = Page(-1, title, '')
			elif "<id>" in line and "</id>" in line and is_first_id:
				page_id = get_id_from_line(line)
				page.page_id = int(page_id)
				is_first_id = False
			elif "<text xml" in line:
				# check if the close tag is in the same line or not
				if "</text>" in line:
					page.content = get_content_from_text_tag('complete', line)
				else:
					# closing tag not in the same line
					page.content = get_content_from_text_tag('opening', line)
					in_text = True
			else:
				if in_text:
					if "</text>" in line:
						page.content = page.content + '\n' +get_content_from_text_tag('closing', line)
						in_text = False
					else:
						page.content = page.content + '\n' + line


f.close()