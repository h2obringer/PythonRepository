#Author: Randal Obringer
#Date Last Modified: 27 September 2016
#Description: Follow the initial url and crawl through its sub sites by the link position
#	and # of iterations provided from the user. Print the path of sites visited as we crawl
#	through the web.
#Course: Coursera via Michigan University - Using Python to Access Web Data

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ') #"Enter - " is the prompt for user input
url = "http://python-data.dr-chuck.net/known_by_Suranne.html"

print "Lets loop through %s and find its url's in a certain position" % url

loopCount = raw_input("# of loops: ")
loopCount = int(loopCount) #ensure it is an integer

position = raw_input("position #: ")
position = int(position)-1 #ensure it is an integer, compensate for 0 start index

sTheLastName="" #hold the last name we parse from scraping the websites

#Note: our given website is our first iteration
for x in xrange(loopCount):
	print "Surfing to: %s" % url
	html = urllib.urlopen(url).read() #read everything in the url to include new lines
	soup = BeautifulSoup(html) #parse the html result

	# Retrieve a list of the anchor tags
	tags = soup('a') #the numbers of comments are given as content of the span tags
	url = tags[position].get('href', None) #set the next url to follow
	sTheLastName = tags[position].contents[0] #hold the last name we saw
#end for loop

print "%s is the last person we saw" % sTheLastName