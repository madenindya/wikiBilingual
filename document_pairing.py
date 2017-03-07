# given set of page-en <--> page-id (link)
# return all links divided by single pair of document

import os.path

# links file
f_link = open('titles_id/en_id_title_result', 'r')
# better to use absolute directory
enwiki_dir = 'output-en/'
idwiki_dir = 'output-id/'
output_dir = 'output-pair/'


def check_file_exists(enwiki, idwiki):
	return os.path.isfile(enwiki_dir + enwiki + '.txt') and os.path.isfile(idwiki_dir + idwiki + '.txt')

for line in f_link:
	line = line.strip()
	if(line == 'id_en/id_id/title_en'):
		continue
	else:
		line = line.split('/')
		enwiki_id = line[0]
		idwiki_id = line[1]
		title = line[2]
		if(check_file_exists(enwiki_id, idwiki_id)):
			# read both file and write into one file
			f = open(enwiki_dir + enwiki_id + '.txt','r')
			out = open(output_dir + title,'w')
			for l in f:
				l = l.strip()
				out.write(l + '\n')
			f.close()
			f = open(idwiki_dir + idwiki_id + '.txt','r')
			for l in f:
				l = l.strip()
				out.write(l + '\n')
			f.close()
			out.close()
		else:
			print 'One of the: (id)',idwiki_id,'or','(en):',enwiki_id,'file does not exist, Continuing to another file...'




f_link.close()