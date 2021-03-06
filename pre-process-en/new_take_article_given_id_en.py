# get the list of id from links-id-en-pages (id of english wikipedia page)

# output supposed to be files which contains only article within the id (smaller version of the original en-wiki)

# assuming ids = list of sorted english wikipedia id

import re

# directory of cleaned file
clean_directory = 'output-clean-en/'
# directory folder of output folder will be
en_ids_directory = 'en_ids.txt'

output_folder = 'output-en/'

def is_beginning_of_page(line):
	return line == '<page>'

def is_end_of_page(line):
	return line == '</page>'

def get_id_title_from_line(line):
	m = re.search('<doc id="(.*)"', line)
	the_id = m.group(1)
	m = re.search('title="(.*)"', line)
	return (the_id, title)

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

## reading section from cleaned directory
arr_of_folder = []

ids_index = 0

for folder in arr_of_folder:
	length = 100
	if folder == #SOME LAST FOLDER:
		length = #SOME INT VALUE OF LAST FILE IN THE LAST FOLDER 
	for i in range(length):
		index = i

		if i < 10:
			index = '0' + str(index)
		f = open(clean_directory + folder + '/wiki_' + index ,'r')

		page = None

		for line in f:
			line = line.strip()
			if "<doc id=" in line and "title=" in line:
				(doc_id, title) = get_id_title_from_line(line)
				while(ids[ids_index] < int(doc_id)):
					ids_index += 1
				if int(ids[ids_index]) == int(doc_id):
					ids_index += 1
					page = Page(int(doc_id), title, '')
				else:
					page = None
			else:
				if page not None:
					if "</doc>" in line:
						# print the page
						page.print_to_file
						print "Completed file :", page.title,"with id", page.page_id
						page = None
						if len(ids) == ids_index:
							print "Done"
							f.close()
							exit()
					else:	
						page.content = page.content + '\n' + line
		f.close()
