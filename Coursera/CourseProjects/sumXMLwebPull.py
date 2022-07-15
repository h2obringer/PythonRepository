#Author: Randal Obringer
#Date Last Modified: 1 October 2016
#Description: pull XML data from the url below. Parse the XML data and sum up the
#	comments data from the XML.
#Course: Coursera via Michigan University - Using Python to Access Web Data

import urllib
import xml.etree.ElementTree as ET

#url = "http://python-data.dr-chuck.net/comments_42.xml"
url = "http://python-data.dr-chuck.net/comments_320372.xml"
xml = urllib.urlopen(url).read() #store the url data as a string

#print xml

xmlData = ET.fromstring(xml) #parse the url data into an XML tree
commentList = xmlData.findall('comments/comment') #create a list of all the "comment"s

iSum = 0 #hold the sum of all comment counts in the XML
for comment in commentList:
	iSum += int(comment.find('count').text) #access the count data in the tree for each comment
#end for loop

print 'The sum of all comments is %d' % iSum