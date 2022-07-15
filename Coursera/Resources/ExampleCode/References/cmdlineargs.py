import sys

print 'Count:', len (sys.argv)
print 'Type:', type(sys.argv)
#sys.argv holds a list of strings where the first string is the name of the Python program
#the remaining strings are the arguments on the command line after the Python file.
for arg in sys.argv:
	print 'Argument:', arg