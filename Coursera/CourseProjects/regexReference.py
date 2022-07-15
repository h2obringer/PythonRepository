# Using regular expressions
#
# import re #is needed to use regular expressions in your program
#
#^ Matches the beginning of a line
# $ Matches the end of the line . Matches any character.
# \s Matches whitespace
# \S Matches any non-whitespace character
# * Repeats a character zero or more times
# *? Repeats a character zero or more times (non-greedy) (uses smallest match)
# + Repeats a character one or more times
# +? Repeats a character one or more times (non-greedy) (uses smallest match)
# [aeiou] Matches a single character in the listed set
# [^XYZ] Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# ( Indicates where string extraction is to start
# ) Indicates where string extraction is to end
#
# re.search() #return true/false if whole string matches
#	i.e. re.search('^From:',x)
# re.findall() #return list extraction of all matching parts of input
#	i.e. re.findall('[0-9]+',x) # return the numbers out of the string
#	i.e. re.findall('^From (\S+@\S+)',x) #return the string in () but starts with a From 

