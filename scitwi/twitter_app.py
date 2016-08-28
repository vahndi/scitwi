import twitter

from scitwi.search.search_response import SearchResponse
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

    def search_tweets(self, query, count=100):
        """
        https://dev.twitter.com/rest/reference/get/search/tweets
        :param query:
        :param count:
        :return:
        """
        search_results = self.api.search.tweets(q=query, count=count)
        return SearchResponse(search_results)
