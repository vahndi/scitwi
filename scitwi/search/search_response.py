from twitter.api import TwitterDictResponse

from scitwi.tweets.tweet import Tweet
from scitwi.utils.strs import obj_string, list_obj_string, obj_string
from .search_metadata import SearchMetadata


class SearchResponse(object):
    """
    https://dev.twitter.com/rest/reference/get/search/tweets
    """
    def __init__(self, response: TwitterDictResponse=None,
                 responses=None):

        assert None in (response, responses)
        if response:
            self._response = response
            self.metadata = SearchMetadata(response['search_metadata'])
            self.statuses = [Tweet(s) for s in response['statuses']]
        else:
            self.metadata = [r.metadata for r in responses]
            self.statuses = [tweet for r in responses for tweet in r.statuses]

    def __str__(self):

        str_out = ''
        if type(self.metadata) is list:
            str_out += list_obj_string('Metadata', self.metadata)
        else:
            str_out += obj_string('Metadata', self.metadata)
        str_out += list_obj_string('Statuses', self.statuses)
        return str_out
