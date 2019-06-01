from tweepy.streaming import StreamListener

class TwitterListener(StreamListener):
    """Required subclass of StreamListener to use Twitter Stream API"""
    def on_data(self, data):
        try:
            with open('Twitter/raw/tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True