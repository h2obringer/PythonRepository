#Using the Twitter API
#Note: need to log into twitter

import urllib
import oauth

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
	
print '* Calling Twitter...'
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
	{'screen_name': 'drchuck', 'count': '2'} )
print url
connection - urllib.urlopen(url)
data = connection.read()
print data
headers = connection.info().dict
print headers
