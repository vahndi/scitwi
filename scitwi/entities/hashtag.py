from typing import List

from scitwi.utils import basic_attr, str_attr, list_int_attr


class Hashtag(object):
    """
    https://dev.twitter.com/overview/api/entities#obj-hashtags
    """
    def __init__(self, hashtag):

        self.indices = list_int_attr(hashtag, 'indices')
        self.text = str_attr(hashtag, 'text')

    def __str__(self):

        str_out = ''
        str_out += 'Indices:\n'
        str_out += '\t%s\n' % self.indices
        str_out += 'Text:\n'
        str_out += '\t%s\n' % self.text

        return str_out
