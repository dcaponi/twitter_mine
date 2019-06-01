from tweepy import OAuthHandler
import config
class TwitterAuth():
    """
        Encapsulates authentication logic and returns an instance of
        the authenticated credentials to enable API methods where
        authentication is required.
    """
    def __init__(self):
        self.auth = OAuthHandler(config.consumer_key, config.consumer_secret)
        self.auth.set_access_token(config.access_token, config.access_secret)
    
    def credentials(self):
        return self.auth