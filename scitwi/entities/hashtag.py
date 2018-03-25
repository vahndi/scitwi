from scitwi.utils.attrs import str_attr, list_int_attr
from scitwi.utils.strs import list_attr_string, obj_string


class Hashtag(object):
    """
    https://dev.twitter.com/overview/api/entities#obj-hashtags
    """
    def __init__(self, hashtag):

        self.indices = list_int_attr(hashtag, 'indices')
        self.text = str_attr(hashtag, 'text')

    def __str__(self):

        str_out = ''
        str_out += list_attr_string('Indices', self.indices, inline=True)
        str_out += obj_string('Text', self.text)
        return str_out
