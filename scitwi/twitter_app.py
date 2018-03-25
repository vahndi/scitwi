from time import sleep
import twitter

from scitwi.places.place_woe import PlaceWOE
from scitwi.search.search_response import SearchResponse
from scitwi.search.types import StrOrQuery
from scitwi.trends import Trends


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
        if count is not None and count <= 100:
            print("searching twitter for '%s'..." % str(query))
            search_results = self.api.search.tweets(q=query, count=count)
            return SearchResponse(response=search_results)
        else:
            finished = False
            num_calls = 0
            num_results = 0
            responses = []
            max_id = None
            sleep_time = 0
            while not finished:
                # sleep to obey rate limit
                sleep(sleep_time)
                num_calls += 1
                # determine how many results to request
                if count is not None:
                    remaining_results = count - num_results
                else:
                    remaining_results = 100
                call_count = min(100, remaining_results)
                # search
                print("searching twitter for '%s' (call %i: %u)..."
                      % (str(query), num_calls, call_count))
                call_results = self.api.search.tweets(
                    q=query, count=call_count, max_id=max_id
                )
                num_results += call_count
                responses.append(SearchResponse(call_results))
                # get the next max_id
                try:
                    max_id = call_results['search_metadata']['max_id']
                except:
                    finished = True
                # calculate sleep time
                rate_limit_remaining = call_results.rate_limit_remaining
                sleep_time = 15 * 60 / rate_limit_remaining
                # exit if all results have been gathered
                if num_results == count:
                    finished = True
            return SearchResponse(responses=responses)
