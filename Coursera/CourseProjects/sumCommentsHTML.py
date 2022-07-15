#Author: Randal Obringer
#Date Last Modified: 27 September 2016
#Description: Scape numbers from the website below using BeautifulSoup. Sum up
#	all of the numbers in the HTML and output that sum.
#Course: Coursera via Michigan University - Using Python to Access Web Data

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ') #"Enter - " is the prompt for user input
url = "http://python-data.dr-chuck.net/comments_320375.html"

html = urllib.urlopen(url).read() #read everything in the url to include new lines
soup = BeautifulSoup(html) #parse the html result

# Retrieve a list of the span tags
tags = soup("span") #the numbers of comments are given as content of the span tags

iSum=0 #hold the sum of all the span tag content essentially accessing the 
	#numbers of comments in the table on the page.
#iterate through all span tags
for tag in tags:
	iSum+=int(tag.contents[0]) #sum up the numbers
	
print "The sum of all comments is %d" % iSum #output
	