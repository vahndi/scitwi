from scitwi.utils.attrs import list_str_attr
from scitwi.utils.strs import list_attr_string


class UserEntitiesDescription(object):

    def __init__(self, description: dict):

        self.urls = list_str_attr(description, 'urls')

    def __str__(self):

        return list_attr_string('Urls', self.urls)
