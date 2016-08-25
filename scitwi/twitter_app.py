import twitter

from scitwi.trends import TwitterTrends
from .places import PlacesWOE


class TwitterApp(object):
    
    def __init__(self,
                 consumer_key: str, consumer_secret: str,
                 oauth_token: str, oauth_token_secret: str):
                     
        auth = twitter.oauth.OAuth(
            oauth_token, oauth_token_secret, consumer_key, consumer_secret
        )
        self.api = twitter.Twitter(auth=auth)

    def get_trends(self, place: PlacesWOE):
        
        trends = self.api.trends.place(_id=str(place.value))
                
        return TwitterTrends(trends)
