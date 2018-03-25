from scitwi.utils.attrs import str_attr, int_attr
from scitwi.utils.strs import obj_string


class Location(object):

    def __init__(self, location: dict):

        self.name = str_attr(location, 'name')
        self.woe_id = int_attr(location, 'woeid')

    def __str__(self):

        str_out = ''
        str_out += obj_string('Name', self.name)
        str_out += obj_string('WOE Id', self.woe_id)
        return str_out
