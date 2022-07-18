#Author: Randal Obringer
#Date Last Modified: 9 December 2016
#Description: Iterate through movie files, find and delete duplicates if the 
#	user agrees.

import re #import for regular expression library
import os
from datetime import datetime


searchLocation = raw_input('Enter the location of the drive to delete duplicates from: ')
print '\nStarting search for duplicate movies in: ', searchLocation

#Start log file for deleted files
movieLog = open('deletedMovieLog.txt','w')
movieLog.truncate() #erase previous contents of file
movieLog.write(str(datetime.now()))
movieLog.write('\n\n')

#log how many movies we find
count = 0

movieList = [] #hold the list of movies
movieList.append('')
duplicate=False

print searchLocation

#start in the Movies directory and recursively walk through all subdirectories
for (dirname, dirs, files) in os.walk(searchLocation):
	#for each file
	for filename in files:
		duplicate=False
		print 'Analyzing ', filename
		for movie in movieList: 
			if (movie==filename):
				print movie, ' = ', filename
				duplicate=True
				performOp = raw_input('Delete the duplicate: ' + filename + '? (y/n)')
			
				if performOp[0]=='y' or performOp[0]=='Y':
					os.remove(os.path.join(dirname,filename)) # remove the duplicate movie
					movieLog.write(filename + ' was deleted. \n')
					print filename, ' was deleted. \n\n'
					count = count+1 #count the number of movies that have been deleted
				
				break
			#end if movie=filename
		#
		if duplicate==False:
			print 'Appending file'
			movieList.append(filename) #this is the first time we have seen the movie, add it to the list of seen movies
		#end movieList for loop
	#end files for loop
#end os.walk() for loop
			
print 'Total # of movies deleted:', count
movieLog.write('Total # of movies deleted: ' + str(count))
movieLog.close()