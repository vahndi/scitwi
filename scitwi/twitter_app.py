import twitter

from scitwi.search.search import Search
from scitwi.trends import Trends
from .places import PlaceWOE
from pprint import pprint


class TwitterApp(object):
    
    def __init__(self,
                 consumer_key: str, consumer_secret: str,
                 oauth_token: str, oauth_token_secret: str):
                     
        auth = twitter.oauth.OAuth(
            oauth_token, oauth_token_secret, consumer_key, consumer_secret
        )
        self.api = twitter.Twitter(auth=auth)

    def get_trends(self, place: PlaceWOE):
        
        trends = self.api.trends.place(_id=str(place.value))
                
        return Trends(trends)

    def search(self, query, count=100):

        search_results = self.api.search.tweets(q=query, count=count)
        return Search(search_results)
