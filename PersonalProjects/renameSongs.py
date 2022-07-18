#Author: Randal Obringer
#Date Last Modified: 19 April 2017
#Description: Iterate through song files and rename them. The main directory 'thePath' is the 
#	entry point for the program to run. All immediate subdirectories have this path structure:
#	Artist/Album/song_name

import re #import for regular expression library
import os
from datetime import datetime

#return a list of names for the immediate subdirectories of the given directory path
def getImmediateSubdirectories(path):
	return [name for name in os.listdir(path)]
	
#return a dictionary containing the file name (theFile) and the file extension (theExtension) 
def splitFile(aFile):
	parsedFile = aFile.split('.')
	currentFile = ''
	currentExtension = ''
	i=0
	
	#ensure the file name is complete if the name has multiple periods
	for part in parsedFile:
		if i!=len(parsedFile)-1:
			currentFile = currentFile + part
		else:
			currentExtension = part
		i=i+1
	
	return { 'theFile':currentFile, 'theExtension':currentExtension }

def removeTrackNumber(aFile):
	#if the file starts with a number or period followed by blank character, then return everything that follows (.+)
	value = re.findall('^[0-9.]+\s(.+)',aFile)
	#value = re.findall('^[0-9][0-9][.]*\s(.+)',aFile)
	return value[0]

#where the program will begin execution
#thePath = raw_input('Enter - ') #"Enter - " is the prompt for user input
thePath = 'F:/Music'

print '\nStarting search for songs in: ', thePath, ' \n'

#Start log file for renamed files
songLog = open('songLog.txt','w')
songLog.truncate() #erase previous contents of file
songLog.write(str(datetime.now()))
songLog.write('\n\n')

#log how many songs we find
count = 0

directories = getImmediateSubdirectories(thePath)

for dir in directories:
	#save the entire directory path so we can continue walking through its subdirectories and files
	current = os.path.join(thePath,dir)
	
	#walk through every subdirectory of thePath
	for (dirname, dirs, files) in os.walk(current):
		for filename in files:
			count = count + 1
			parts = splitFile(filename)
			
			try:
				#come up with the new file name with the track # removed and the artist name added
				newFile = removeTrackNumber(parts['theFile']) + ' - ' + dir + '.' + parts['theExtension']
				
				#uncomment to control renaming each file or not
				#performOp = raw_input('Rename ' + filename + '\n to: \n' + newFile + '? (y/n)\n')
				#if performOp[0]=='y' or performOp[0]=='Y':
				
				os.rename(os.path.join(dirname,filename), os.path.join(dirname,newFile)) #rename the file to the new file name
				songLog.write(filename + ' was renamed to: ' + newFile + '\n')
				print filename, ' was renamed to: ', newFile, '\n\n'
				#end if
				
			except:
				print 'Caught the error, nothing was executed for: ', filename
				continue
	#end files for loop
#end os.walk() for loop
			
#print 'Total # of movie dates found:', count
songLog.close()