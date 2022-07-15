#Author: Randal Obringer
#Date Last Modified: 1 October 2016
#Description: Access the url below and parse the json data. Sum up the comments 
#	provided in the json data.
#Course: Coursera via Michigan University - Using Python to Access Web Data

import json
import urllib

#url = "http://python-data.dr-chuck.net/comments_42.json"
url = "http://python-data.dr-chuck.net/comments_320376.json"
handle = urllib.urlopen(url)
data = handle.read()

try: info = json.loads(data) #try to parse the json
except: info = None
if 'comments' not in info or info is None: #if exception happened
	print '==== Failure To Retrieve ==='
	print data
	quit()
#end if

#print json.dumps(info, indent=4) #take the parsed dictionary and print it out nicely with indent 4

iSum = 0 #hold the sum of comment counts in the json data
for comment in info["comments"]:
	#print 'Name', comment["name"]
	#print 'Count', comment["count"]
	iSum += int(comment["count"])
#end for loop

print "Sum of comments is %d" % iSum 