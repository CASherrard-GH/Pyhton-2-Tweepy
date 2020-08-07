from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)
        
        
if name__ == "__main__":
    
    listener = StdOutListener()
    auth = OAuthHandler(twitter credentials.CONSUMER KEY, twitter credentials.CONSUMER SECRET)
    auth.set access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
                        (param auth, param_listener, param **options)
    stream = Stream(auth, listener)
    
    stream.filter(track=['elon musk', 'bill gates', 'jeff bezos'])