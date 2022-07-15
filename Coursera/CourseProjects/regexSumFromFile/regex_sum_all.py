#Author: Randal Obringer
#Date Last Modified: 26 September 2016
#Description: Parse a file and sum up all numbers in the file. Find numbers 
#	using regular expressions. Return the sum of all numbers.
#Course: Coursera via Michigan University - Using Python to Access Web Data

import re #import for regular expression library

theFile = open('regex_sum_320370.txt')
iSum=0 #holds the overall sum of the numbers we find in the file

for line in theFile: #for each line the the file we opened
	line = line.rstrip() #remove white space from end of each line
	foundMatches = re.findall('([0-9]+)',line) #find the numbers in the line
	
	if len(foundMatches) == 0 : continue #we don't care about empty lists
	
	for i in xrange(len(foundMatches)): #for each number in the current list
		iSum += int(foundMatches[i]) #add the numbers to the running total
	#end for loop
#end for loop

print "The sum of all numbers in the file is: %d" % iSum
