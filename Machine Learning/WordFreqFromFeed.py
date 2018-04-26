import feedparser as fp
import re          

#Returns title and dictionary of word frequecy of a RSS Feed

def getwordcounts(url):
	#Parse the feed into text
	d = fp.parse(url)
	wc = {}
	
	# Loop over all entries
	for e in d.entries:
		if 'summary' in e: summary = e.summary
		else: summary = e.description
		
		#Extract a list of words
		words = getwords(e.title + ' ' +summary)
		for word in words:
			wc.setdefault(word,0)
			wc[word]+=1
	return d.feed.title,wc


def getwords(html):
	#Remove all the HTML tags
	txt = re.compile(r'<[^>]+>').sub('',html)

	#Split words by non-alpha split when anything other than A-Z or a-b appears
	# ^ - negation 
	words = re.compile(r'[^A-Z^a-z]').split(txt)

	return [word.lower() for word in words if word != '']

apcount = {} #count if word appears in more than one block
wordcounts = {}
for feedurl in file(''):
	title,wc = getwordcounts(feedurl)
	wordcounts[title] = wc
	for word,count in wc.items():
		apcount.setdefault(word,0)
		if(count>1):
			apcount[word] += 1
		
wordlist = []
for w,c in apcount.items():
	frac = float(c)/len(filename)
	if frac > 0.1 and frac < 0.5 wordlist.append(w)

out = file('blog.txt',w)
out.write('Blog')
for word in wordlist: 
	out.write('\t%s'%word)
out.write('\n')
for blog,wc in wordcounts.items():
	out.write(blog)
	for word in wordlist:
		if word in wc:	out.write('\t%d'% wc[word])
		else: out.write('\t0')
	out.write('\n')
		
