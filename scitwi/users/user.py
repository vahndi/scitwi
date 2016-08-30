from scitwi.users.user_entities import UserEntities
from scitwi.users.user_profile import UserProfile
from scitwi.utils.attrs import bool_attr, datetime_attr, str_attr, obj_attr
from scitwi.utils.attrs import int_attr
from scitwi.utils.strs import attr_string


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

    def __str__(self):

        str_out = ''

        str_out += attr_string('Contributors Enabled', self.contributors_enabled)
        str_out += attr_string('Created At', self.created_at)
        str_out += attr_string('Default Profile', self.default_profile)
        str_out += attr_string('Default Profile Image', self.default_profile_image)
        str_out += attr_string('Description', self.description)
        str_out += attr_string('Entities', self.entities)
        str_out += attr_string('Favourites Count', self.favourites_count)
        str_out += attr_string('Follow Request Sent', self.follow_request_sent)
        str_out += attr_string('Following', self.following)
        str_out += attr_string('Followers Count', self.followers_count)
        str_out += attr_string('Friends Count', self.friends_count)
        str_out += attr_string('Geo Enabled', self.geo_enabled)
        str_out += attr_string('Has Extended Profile', self.has_extended_profile)
        str_out += attr_string('Id', self.id_)
        str_out += attr_string('Is Translation Enabled', self.is_translation_enabled)
        str_out += attr_string('Is Translator', self.is_translator)
        str_out += attr_string('Language', self.lang)
        str_out += attr_string('Listed Count', self.listed_count)
        str_out += attr_string('Location', self.location)
        str_out += attr_string('Name', self.listed_count)
        str_out += attr_string('Notifications', self.notifications)
        str_out += attr_string('Profile', self.profile)
        str_out += attr_string('Protected', self.protected)
        str_out += attr_string('Screen Name', self.screen_name)
        str_out += attr_string('Show All Inline Media', self.show_all_inline_media)
        str_out += attr_string('Statuses Count', self.statuses_count)
        str_out += attr_string('Time Zone', self.time_zone)
        str_out += attr_string('Url', self.url)
        str_out += attr_string('UTC Offset', self.utc_offset)
        str_out += attr_string('Verified', self.verified)

        return str_out


