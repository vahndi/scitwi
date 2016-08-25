import twitter

from .twitter_trends import TwitterTrends
from .places import PlacesWOE


class TwitterApp(object):
    
    def __init__(self, 
                 CONSUMER_KEY, CONSUMER_SECRET, 
                 OAUTH_TOKEN, OAUTH_TOKEN_SECRET):
                     
        auth = twitter.oauth.OAuth(
            OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
        )
        self.api = twitter.Twitter(auth=auth)

    def get_trends(self, place: PlacesWOE):
        
        trends = self.api.trends.place(_id=str(place.value))
                
        return TwitterTrends(trends)
