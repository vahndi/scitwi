from scitwi.users.user_entities import UserEntities
from scitwi.users.user_profile import UserProfile
from scitwi.utils import get_datetime


class User(object):

    def __init__(self, user: dict):

        self.contributors_enabled = user['contributors_enabled']
        self.created_at = get_datetime(user['created_at'])
        self.default_profile = user['default_profile']
        self.default_profile_image = user['default_profile_image']
        self.description = user['description']
        self.entities = UserEntities(user['entities'])
        self.favourites_count = user['favourites_count']
        self.follow_request_sent = user['follow_request_sent']
        self.followers_count = user['followers_count']
        self.following = user['following']
        self.friends_count = user['friends_count']
        self.geo_enabled = user['geo_enabled']
        self.has_extended_profile = user['has_extended_profile']
        self.id_ = user['id']
        self.is_translation_enabled = user['is_translation_enabled']
        self.is_translator = user['is_translator']
        self.lang = user['lang']
        self.listed_count = user['listed_count']
        self.location = user['location']
        self.name = user['name']
        self.notifications = user['notifications']
        self.profile = UserProfile(user)
        self.protected = user['protected']
        self.screen_name = user['screen_name']
        self.statuses_count = user['statuses_count']
        self.time_zone = user['time_zone']
        self.url = user['url']
        self.utc_offset = user['utc_offset']
        self.verified = user['verified']



