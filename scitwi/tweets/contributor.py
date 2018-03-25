from scitwi.utils.attrs import int_attr, str_attr
from scitwi.utils.strs import obj_string


class Contributor(object):
    """
    https://dev.twitter.com/overview/api/tweets#obj-contributors
    """
    def __init__(self, contributor: dict):

        self.id_ = int_attr(contributor, 'id')
        self.screen_name = str_attr(contributor, 'screen_name')

    def __str__(self):

        str_out = ''
        str_out += obj_string('Id', self.id_)
        str_out += obj_string('Screen Name', self.screen_name)
