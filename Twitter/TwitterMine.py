from Twitter.TwitterListener import TwitterListener
import tweepy
from tweepy import Stream
from Twitter.TwitterAuth import TwitterAuth

class TwitterMine:
    def __init__(self):
        self.authenticator = TwitterAuth()
    
    def api(self, options=None):
        if self.api is None:
            self.api = tweepy.API(self.authenticator.credentials())
        return self.api
    
    def start_stream(self, options=None):
        self.stream = Stream(self.authenticator.credentials(), TwitterListener())
        if options:
            print("tracking the options {}".format(options))
            self.stream.filter(track=options)
        return self.stream