#Author: Randal Obringer
#Description: Delete unwanted files in all of my repositories on my computer.
#	This file is written and setup to be run from the below location:
#		C:\Users\Obringer-Computer\Desktop\Programming\Python\PythonRepository\code
#	It will start execution at the "Pogramming" directory and clean up files such 
#	as .o, anything ending with ~, and .h.gch.
#Date Last Modified: 23 October 2016

import os
from datetime import datetime

#inventory how many unwanted files are in the subfolders using the program
count = 0

print '\nStarting cleanup of files from directory: \n', os.path.abspath('../../../')

answer = raw_input('\nContinue? y/n \n')
if(answer=='n' or answer=='N'):
	quit()
	
#Start log file for deleted files
deletionLog = open('deletionLog.txt','w')
deletionLog.truncate() #erase previous contents of file

deletionLog.write(str(datetime.now()))
deletionLog.write('\n\n')
deletionLog.write('Deleted the following files:\n\n')

#start 3 directories up and recursively walk through all subdirectories
for (dirname, dirs, files) in os.walk('../../../'): 
	#for each file
	for filename in files:
		#for the following file types
		if filename.endswith('.o') or filename.endswith('~') or filename.endswith('.h.gch'):
			theFile = os.path.join(dirname,filename) #log the file, join allows the program to operate on windows and linux.
			count = count+1
			os.remove(theFile) #deletes the found file
			print 'Deleted file: ', theFile
			deletionLog.write('-' + theFile + '\n')
			
print 'Total # of files deleted:', count
deletionLog.close()

#os.remove(theFile) #deletes the file
