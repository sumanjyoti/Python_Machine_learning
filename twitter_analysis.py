import tweepy
from textblob import TextBlob

# changed for security
consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

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
