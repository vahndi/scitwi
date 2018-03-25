from scitwi.users.user_entities_description import UserEntitiesDescription
from scitwi.users.user_entities_url import UserEntitiesUrl
from scitwi.utils.attrs import obj_attr
from scitwi.utils.strs import obj_string


class UserEntities(object):

    def __init__(self, entities: dict):

        self.description = obj_attr(entities, 'description', UserEntitiesDescription)
        self.url = obj_attr(entities, 'url', UserEntitiesUrl)

    def __str__(self):

        str_out = ''
        str_out += obj_string('Description', self.description)
        str_out += obj_string('Url', self.url)
        return str_out
