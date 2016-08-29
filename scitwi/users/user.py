from scitwi.users.user_entities import UserEntities
from scitwi.users.user_profile import UserProfile
from scitwi.utils.attrs import bool_attr, datetime_attr, str_attr, obj_attr
from scitwi.utils.attrs import int_attr


class User(object):
    """
    Users can be anyone or anything. They tweet, follow, create lists,
    have a home_timeline, can be mentioned, and can be looked up in bulk.

    https://dev.twitter.com/overview/api/users
    """
    def __init__(self, user: dict):

        self.contributors_enabled = bool_attr(user, 'contributors_enabled')
        self.created_at = datetime_attr(user, 'created_at')
        self.default_profile = bool_attr(user, 'default_profile')
        self.default_profile_image = bool_attr(user, 'default_profile_image')
        self.description = str_attr(user, 'description')
        self.entities = obj_attr(user, 'entities', UserEntities)
        self.favourites_count = int_attr(user, 'favourites_count')
        self.follow_request_sent = bool_attr(user, 'follow_request_sent')
        self.following = bool_attr(user, 'following')  # deprecated
        self.followers_count = int_attr(user, 'followers_count')
        self.friends_count = int_attr(user, 'friends_count')
        self.geo_enabled = bool_attr(user, 'geo_enabled')
        self.has_extended_profile = bool_attr(user, 'has_extended_profile')
        self.id_ = int_attr(user, 'id')
        self.is_translation_enabled = bool_attr(user, 'is_translation_enabled')  # not in docs
        self.is_translator = bool_attr(user, 'is_translator')
        self.lang = str_attr(user, 'lang')
        self.listed_count = int_attr(user, 'listed_count')
        self.location = str_attr(user, 'location')
        self.name = str_attr(user, 'name')
        self.notifications = bool_attr(user, 'notifications')  # deprecated
        self.profile = UserProfile(user)
        self.protected = bool_attr(user, 'protected')
        self.screen_name = str_attr(user, 'screen_name')
        self.show_all_inline_media = bool_attr(user, 'show_all_inline_media')
        self.statuses_count = user['statuses_count']
        self.time_zone = user['time_zone']
        self.url = user['url']
        self.utc_offset = user['utc_offset']
        self.verified = user['verified']



