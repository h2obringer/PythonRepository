import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ') #"Enter - " is the prompt for user input
url = "http://www.dr-chuck.com/"

html = urllib.urlopen(url).read() #read everything in the url to include new lines
soup = BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('a')

for tag in tags:
	print 'TAG:',tag
	print 'URL:',tag.get('href',None)
	print 'Contents:',tag.contents[0]
	print 'Attrs:',tag.attrs