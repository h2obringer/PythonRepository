import urllib

#this does the same thing as the socket call but does not return the header/meta data
handle = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

counts = dict()
for line in handle:
	print line.strip()
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1 #count frequency of words in the url file
print counts
	
	