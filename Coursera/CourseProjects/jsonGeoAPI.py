#Author: Randal Obringer
#Date Last Modified: 1 October 2016
#Description: Access the url below for a static version of the google geo API.
#	Properly send parameters in the url in the request and receive JSON data.
#	Parse the JSON data for the place_id of the location the user enters and return it.
#Course: Coursera via Michigan University - Using Python to Access Web Data

import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?' #The ? is needed to add the parameters

while True:
	address = raw_input('Enter location: ')
	if len(address) < 1 : break
	
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address}) #encode the paramters in the url for us 
	print 'Retrieving', url
	handle = urllib.urlopen(url)
	data = handle.read()
	
	print 'Retrieved',len(data),'characters'
	
	try: info = json.loads(str(data)) #try to parse the json
	except: info = None
	if info is None or 'status' not in info or info['status'] != 'OK': #if exception happened or status not ok
		print '==== Failure To Retrieve ==='
		print data
		quit()
	#end if
	#print json.dumps(info, indent=4) #take the parsed dictionary and print it out nicely with indent 4
	
	id = info['results'][0]['place_id'] #access the first result element and find the place_id
	print "ID: ", id