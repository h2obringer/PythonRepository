import urllib
import oauth
import json

#this authorizes an application not a user to use the twitter interface
#WILL NOT work until you get your own application key/token 
def oauth(): #must get the application token from twitter. 
	#You would want to keep this stuff hidden so others cannot use it. 
	return {
		"consumer_key" : "",
		"consumer_secret" : "",
		"token_key" : "",
		"token_secret" : ""}

#add the parameters and signature to the url for oauth
def augment(url, parameters): #parameters is a dictionary
	secrets = oauth()
	consumer = oath.OAuthConsumer(secrets['consumer_key'],secrets['consumer_secret']);
	token = oauth.OAuthToken(secrets['token_key'],secrets['token_secret'])
	oauth_request = oath.OAuthRequest.from_xonsumer_and_token(consumer,token=token, 
		http_method='GET', http_url=url, parameters=parameters)
	oauth_request.sign_request(oath.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
	return oauth_request.to_url()
	
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
	print ''
	acct = raw_input("Enter Twitter Account:")
	if (len(acct) < 1 ) : break
	url = augment(TWITTER_URL, {'screen_name': acct, 'count' : 't'} )
	print 'Retrieving', url
	connection - urllib.urlopen(url)
	data = connection.read()
	headers = connection.info().dict
	print 'Remaining usage cap', headers['x-rate-limit-remaining']
	js = json.loads(data)
	print jason.dumps(js, indent=4) #print json in readable format
	for u in js['users']: #go through list of all user friends
		print u['screen_name']
		s = u['status']['text']
		print '   ', s[:50] #print first 50 characters of status