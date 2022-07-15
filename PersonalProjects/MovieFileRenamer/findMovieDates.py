#Author: Randal Obringer
#Date Last Modified: 22 November 2016
#Description: Iterate through movie files, find movies not labeled with a date,
#	surf IMDb's website for the date, and append the date to the movie file

import urllib
import re #import for regular expression library
import os
from datetime import datetime
from BeautifulSoup import *

#serviceurl = "http://www.imdb.com/find?ref_=nv_sr_fn&q=movie_title&s=all"
serviceurl = "http://www.imdb.com/find?"

#searchLocation = raw_input('Enter - ') #"Enter - " is the prompt for user input
#print '\nStarting search of movie dates in: ', searchLocation

print '\nStarting search of movie dates in: G:/Movies \n'

#Start log file for deleted files
movieLog = open('movieLog.txt','w')
movieLog.truncate() #erase previous contents of file
movieLog.write(str(datetime.now()))
movieLog.write('\n\n')

#log how many movies we find
count = 0

#start in the Movies directory and recursively walk through all subdirectories
for (dirname, dirs, files) in os.walk('G:/Movies'): 
#for (dirname, dirs, files) in os.walk('C:/Users/Obringer-Computer/Desktop/test'): #TEST LOOP
	#for each file
	for filename in files:
		count = count+1
		
		
		#if files have multiple '.' then we want to split at the last one
		parsedFile = filename.split('.')
		theFile = ''
		theExtension = ''
		i=0
		for part in parsedFile:
			if i!=len(parsedFile)-1:
				theFile = theFile + part
			else:
				theExtension = part
			i=i+1
		#print 'File name: ', theFile
		#print 'Extension: ', theExtension
		
		
		
		#theFile = filename.split('.')[0] #retrieve only the file name without the extension
		#theExtension = filename.split('.')[1] #retrieve only the file extension without the '.'
		
		if re.search('[(][0-9]+[)]',theFile): #if the title already is labeled with the date then skip it
			#print theFile, ' should NOT be found and renamed'
			movieLog.write(filename + ' was NOT renamed \n')
			continue #move on to the next movie
		
		#print theFile, ' should be found and renamed'
		
		try:
			#match the file with date on end
			print 'Looking up date for: ', theFile
			url = serviceurl + urllib.urlencode({'ref_':'nv_sr_fn', 'q':theFile, 's':'titles'}) #encode the parameters in the url for us 
			html = urllib.urlopen(url).read() #retrieve the html from the url
			soup = BeautifulSoup(html) #parse the html
			
			#TARGET SECTION IN RESULTING HTML
				#<body> <div id="wrapper"> <div id="root"> <div id="content-2-wide"> <div id="main"> <div class="article"> 
				#<div class="findSection"> <table class="findList"> <td class="result_text">
			resultList = soup.findAll("td", { "class" : "result_text" }) #will produce HTML in the following format: <td><a href="">Title</a> Year </td>, the year is our target
				
			#result is the year to append to the filename, if no result then this will produce an IndexError
			result = resultList[0].contents[2] #grabs only the top result from the search, skips <td> and <a> tags, pulls the date that we are looking for
		
			newFile = theFile + result.rstrip() + '.' + theExtension #create the name of the new file with the date we found added to it
			
			performOp = raw_input('Rename ' + filename + ' to: ' + newFile + '? (y/n)')
			
			if performOp[0]=='y' or performOp[0]=='Y':
				os.rename(os.path.join(dirname,filename), os.path.join(dirname,newFile)) #rename the file to the new file name
				movieLog.write(filename + ' was renamed to: ' + newFile + '\n')
				print filename, ' was renamed to: ', newFile, '\n'
			#end if
			
			#TODO
			#else:
				#try next in the result list for the same movie because we might not have gotten the result we wanted
		except IndexError:
			print 'Caught the IndexError, no result was found for ', filename
			continue
	#end files for loop
#end os.walk() for loop
			
#print 'Total # of movie dates found:', count
movieLog.close()