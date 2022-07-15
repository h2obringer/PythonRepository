#Note: using APIs are not always free. API Security and Rate Limiting is applied
#	or a key is required meaning you paid for it. Check the API documentation.
#use the google search engine to take user entered location and return the location data

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = raw_input('Enter location: ')
	if len(address) < 1 : break
	
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address}) #encode the data in the url for us for what is expected in the url
	print 'Retrieving', url
	handle = urllib.urlopen(url)
	data = handle.read()
	print 'Retrieved',len(data),'characters'
	
	try: js = json.loads(str(data)) #try to parse the json
	except: js = None
	if 'status' not in js or js['status'] != 'OK': #if exception happened or status not ok
		print '==== Failure To Retrieve ==='
		print data
		continue #start the loop again
	#end if
	print json.dumps(js, indent=4) #take the parsed dictionary and print it out nicely with indent 4
	
	lat = js["results"][0]["geometry"]["location"]["lat"] #parse for latitude, just grab the first in the list
	lon = js["results"][0]["geometry"]["location"]["lng"] #parse for longitude, just grab the first in the list
	print 'lat',lat,'lon',lon
	location = js['results'][0]['formatted_address'] #parse for location
	print location