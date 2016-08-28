from scitwi.utils.attrs import str_attr
from scitwi.utils.strs import attr_string


class CurrentUserRetweet(object):

    def __init__(self, current_user_retweet: dict):

        self. id_ = str_attr(current_user_retweet, 'id')

    def __str__(self):

        return attr_string(self.id_)
