from twitter.api import TwitterDictResponse

from scitwi.status.status import Status
from .search_metadata import SearchMetadata


class Search(object):

    def __init__(self, response: TwitterDictResponse):

        self._response = response
        self.metadata = SearchMetadata(response['search_metadata'])
        self.statuses = [Status(s) for s in response['statuses']]
