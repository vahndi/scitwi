import twitter

from scitwi.search.search_response import SearchResponse
from scitwi.search.types import StrOrQuery
from scitwi.trends import Trends
from .places import PlaceWOE


class TwitterApp(object):
    
    def __init__(self,
                 consumer_key: str, consumer_secret: str,
                 oauth_token: str, oauth_token_secret: str):
        """
        Create a new Twitter Application instance using the details given.
        """
        auth = twitter.oauth.OAuth(
            oauth_token, oauth_token_secret, consumer_key, consumer_secret
        )
        self.api = twitter.Twitter(auth=auth)

    def get_trends(self, place: PlaceWOE):
        """
        Return a list of Trends for a given place.

        :param place: The place to search for Trends in.
        :rtype: Trends
        """
        trends = self.api.trends.place(_id=str(place.value))
        return Trends(trends)

    def search_tweets(self, query: StrOrQuery, count: int=100):
        """
        https://dev.twitter.com/rest/reference/get/search/tweets
        """
        print("searching twitter for '%s'..." % str(query))
        search_results = self.api.search.tweets(q=query, count=count)
        return SearchResponse(search_results)
