import xml.etree.ElementTree as ET

#uses a triple quote so we can use double and single quotes within the string
data = ''' 
<person>
	<name>Chuck</name>
	<phone type="intl">
		+1 734 303 4456
	</phone>
	<email hide="yes"/>
</person>'''

tree = ET.fromstring(data) #parsing/deserialization
print 'Name:', tree.find('name').text
print "Attr:', tree.find('email').get('hide')
