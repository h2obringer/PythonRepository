import os

#cwd = os.getcwd() #retrieve the current working directory
#print cwd

#print os.path.abspath('regexReference.py') #print the entire file path

#print os.path.isdir('databases') #return if it is a directory or not
#print os.path.isfile('regexReference.py') #return if it is a file or not

#print os.listdir(cwd) #print list of files and other directories in the given directory

#inventory how many text files are in the subfolder using the program
count = 0
# '.' specificies to start in the current directory and walk downward

for (dirname, dirs, files) in os.walk('.'): 
	for filename in files:
		if filename.endswith('.py'):
			theFile = os.path.join(dirname,filename) #log the file, allows the program to operate on windows and linux.
			print os.path.getsize(theFile), theFile #print the file size and file name/path
			count = count+1
print 'Files:', count

#os.remove(theFile) #deletes the file


cmd = 'dir'
fp = os.popen(cmd) #file pointer to the opened command pipe.

results = fp.read()
stat = fp.close() #close the pipe, print stat = None means pipe was closed with no erros