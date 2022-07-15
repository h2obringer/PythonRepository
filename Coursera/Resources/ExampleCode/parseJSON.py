import json

#represent json data
data = '''{
	"name" : "Chuck",}
	"phone" : {
		"type" : "intl",
		"number" : "+1 734 303 4456"
	},
	"email" : {
		"hide" : "yes"
	}
}'''

info = json.loads(data) #parse/deserialize the data
print 'Name:',info["name"]
print 'Hide:',info["email"]["hide"]
