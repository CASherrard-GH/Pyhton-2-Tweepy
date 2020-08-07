import tweepy
from tweepy import OAuthHandler
 
consumer_key = '0yuBjWl7fZP23pijhj25n8Umn'
consumer_secret = 'ZRmyxNlVwCYR2dMMUEaXZhKl1goeSHd610hR7ouEmbe1MwUfjY'
access_token = '843081371925057536-WlhfAZJOIyetDnsSERSbBjJMZ7XGYv4'
access_secret = 'Jb0XK0pOUbfji4nKwe4CNCWsvzq8HcicCYB84ZwjyBkbK'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)