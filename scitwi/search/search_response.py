import gzip
import pickle
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

        if self.statuses:
            return min([tweet.id_ for tweet in self.statuses])
        return None

    @property
    def num_tweets(self):
        return len(self.statuses)

    def save(self, file_path: str, compress: bool):
        """
        Save the response object to disk.

        :param file_path: The path to the file to save.
        :param compress: Whether to compress the file with gzip.
        """
        out_obj = self._response if self._response else self._responses
        if compress:
            f = gzip.open(file_path, 'wb')
            pickle.dump(out_obj, f)
            f.close()
        else:
            pickle.dump(out_obj, open(file_path, 'wb'))

    @classmethod
    def load(cls, file_path: str, compressed: bool):
        """
        Load a response from disk and return a new SearchResponse.

        :param file_path: The path to the file to load.
        :param compressed: Whether the file is compressed with gzip.
        :rtype: SearchResponse
        """
        # load file
        if compressed:
            f = gzip.open(file_path, 'rb')
            response = pickle.load(f)
            f.close()
        else:
            response = pickle.load(open(file_path, 'rb'))
        # return new SearchResponse instance
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
