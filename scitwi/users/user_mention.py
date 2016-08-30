from scitwi.utils.attrs import int_attr, list_int_attr, str_attr
from scitwi.utils.strs import attr_string, list_attr_string


class UserMention(object):

    def __init__(self, user_mention: dict):

        self.id_ = int_attr(user_mention, 'id')
        self.indices = list_int_attr(user_mention, 'indices')
        self.name = str_attr(user_mention, 'name')
        self.screen_name = str_attr(user_mention, 'screen_name')

    def __str__(self):

        str_out = ''
        str_out += attr_string('Id', self.id_)
        str_out += list_attr_string('Indices', self.indices)
        str_out += attr_string('Name', self.name)
        str_out += attr_string('Screen Name', self.screen_name)
        return str_out
