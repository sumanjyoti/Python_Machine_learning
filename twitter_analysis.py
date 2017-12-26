import tweepy
from textblob import TextBlob

# changed for security
consumer_key = "XXCkFqftqHZtCQsEyTnIqi1cu"
consumer_secret = "dhe30Ya7KWoa9TQMmoHFZlrW66GIJWucyy7bcGsrZKVGR9nsSm"

access_token = "860302969-ekxjcHqyHajykJnHNwGkf1gMrULZqrYQEkP6Lt33"
access_token_secret = "lPX8oRBbu1i4q46bO8Rgs3DEUSpDW89ZT2oC5ZfOngak7"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#public_tweets = api.search('snappyjyoti')
#public_tweets = api.search('benaffleck')
#public_tweets = api.search('Trump')
public_tweets = api.search('Padmavati')
for tweet in public_tweets:
  print(tweet.text)
  analysis = TextBlob(tweet.text)
  print(analysis.sentiment)
