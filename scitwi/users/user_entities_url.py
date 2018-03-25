from scitwi.users.user_entities_url_url import UserEntitiesUrlUrl
from scitwi.utils.attrs import list_obj_attr
from scitwi.utils.strs import obj_string, list_obj_string


class UserEntitiesUrl(object):

    def __init__(self, url: dict):

        self.urls = list_obj_attr(url, 'urls', UserEntitiesUrlUrl)

    def __str__(self):

        return list_obj_string('Urls', self.urls)
