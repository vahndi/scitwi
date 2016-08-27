from scitwi.users.user_description_entity import UserDescriptionEntity


class UserEntities(object):

    def __init__(self, entities: dict):

        self.description = UserDescriptionEntity(entities['description'])
