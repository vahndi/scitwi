from twitter.api import TwitterDictResponse

from scitwi.status.status import Status
from scitwi.utils.strs import attr_string
from .search_metadata import SearchMetadata


class SearchResponse(object):
    """
    https://dev.twitter.com/rest/reference/get/search/tweets
    """
    def __init__(self, response: TwitterDictResponse):

        self._response = response
        self.metadata = SearchMetadata(response['search_metadata'])
        self.statuses = [Status(s) for s in response['statuses']]

    def __str__(self):

        str_out = ''
        str_out += attr_string('Metadata', self.metadata)
        str_out += attr_string('Statuses', self.statuses)
        return str_out
