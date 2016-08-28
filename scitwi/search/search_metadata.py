from scitwi.utils.attrs import float_attr, int_attr, str_attr
from scitwi.utils.strs import attr_string


class SearchMetadata(object):
    """
    https://dev.twitter.com/rest/reference/get/search/tweets
    """
    def __init__(self, metadata: dict):

        self.completed_in = float_attr(metadata, 'completed_in')
        self.count = int_attr(metadata, 'count')
        self.max_id = int_attr(metadata, 'max_id')
        self.next_results = str_attr(metadata, 'next_results')
        self.query = str_attr(metadata, 'query')
        self.refresh_url = str_attr(metadata, 'refresh_url')
        self.since_id = int_attr(metadata, 'since_id')

    def __str__(self):

        str_out = ''
        str_out += attr_string('Completed In', self.completed_in)
        str_out += attr_string('Count', self.count)
        str_out += attr_string('Max Id', self.max_id)
        str_out += attr_string('Next Results', self.next_results)
        str_out += attr_string('Query', self.query)
        str_out += attr_string('Refresh Url', self.refresh_url)
        str_out += attr_string('Since Id', self.since_id)
        return str_out

