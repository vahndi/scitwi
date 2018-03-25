from scitwi.utils.attrs import str_attr, list_int_attr
from scitwi.utils.strs import obj_string, list_obj_string


class UserEntitiesUrlUrl(object):

    def __init__(self, url: dict):

        self.url = str_attr(url, 'url')
        self.expanded_url = str_attr(url, 'expanded_url')
        self.indices = list_int_attr(url, 'indices')

    def __str__(self):

        str_out = ''
        str_out += obj_string('Url', self.url)
        str_out += obj_string('Expanded Url', self.expanded_url)
        str_out += list_obj_string('Indices', self.indices)
        return str_out
