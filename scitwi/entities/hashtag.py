from typing import List


class Hashtag(object):
    """
    https://dev.twitter.com/overview/api/entities#obj-hashtags
    """
    def __init__(self, hashtag):

        self.indices = hashtag['indices']  # type: List[int]
        self.text = hashtag['text']  # type: str

    def __str__(self):

        str_out = ''
        str_out += 'Indices:\n'
        str_out += '\t%s\n' % self.indices
        str_out += 'Text:\n'
        str_out += '\t%s\n' % self.text

        return str_out
