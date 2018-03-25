from pickle import dump, load
from twitter.api import TwitterDictResponse

from scitwi.tweets.tweet import Tweet
from scitwi.utils.strs import obj_string, list_obj_string, obj_string
from .search_metadata import SearchMetadata


class SearchResponse(object):
    """
    https://dev.twitter.com/rest/reference/get/search/tweets
    """
    def __init__(self, response: TwitterDictResponse=None,
                 responses: list=None):

        self._response = None
        self._responses = None

        assert None in (response, responses)
        if response:
            self._response = response
            self.metadata = SearchMetadata(response['search_metadata'])
            self.statuses = [Tweet(s) for s in response['statuses']]
        else:
            self._responses = responses
            self.metadata = [r.metadata for r in responses]
            self.statuses = [tweet for r in responses for tweet in r.statuses]

    def min_id(self):

        tweet_ids = [tweet.id_ for tweet in self.statuses]
        return min(tweet_ids)

    def save(self, file_path: str):
        """
        Save the response object to disk.

        :param file_path: The path to the file to save.
        """
        if self._response:
            dump(self._response, open(file_path, 'wb'))
        else:
            dump(self._responses, open(file_path, 'wb'))

    @classmethod
    def load(cls, file_path: str):
        """
        Load a response from disk and return a new SearchResponse.

        :param file_path:
        :rtype: SearchResponse
        """
        response = load(open(file_path, 'rb'))
        if type(response) is TwitterDictResponse:
            return cls(response=response)
        elif type(response) is list:
            return cls(responses=response)

    def __str__(self):

        str_out = ''
        if type(self.metadata) is list:
            str_out += list_obj_string('Metadata', self.metadata)
        else:
            str_out += obj_string('Metadata', self.metadata)
        str_out += list_obj_string('Statuses', self.statuses)
        return str_out
