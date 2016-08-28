from scitwi.entities.entities import Entities
from scitwi.places.geo import Geo
from scitwi.places.place import Place
from scitwi.tweets.contributor import Contributor
from scitwi.tweets.current_user_retweet import CurrentUserRetweet
from scitwi.users.user import User
from scitwi.utils.attrs import list_obj_attr, obj_attr, datetime_attr, int_attr, bool_attr, str_attr, dict_attr


class Tweet(object):
    """
    https://dev.twitter.com/overview/api/tweets
    """
    def __init__(self, tweet: dict):

        self.contributors = list_obj_attr(tweet, 'contributors', Contributor)
        self.coordinates = obj_attr(tweet, 'coordinates', Geo)
        self.created_at = datetime_attr(tweet, 'created_at')
        self.current_user_retweet = obj_attr(tweet, 'current_user_retweet', CurrentUserRetweet)
        self.entities = obj_attr(tweet, 'entities', Entities)
        self.favorite_count = int_attr(tweet, 'favorite_count')
        self.favorited = bool_attr(tweet, 'favorited')
        self.filter_level = str_attr(tweet, 'filter_level')
        self.geo = obj_attr(tweet, 'geo', Geo)  # deprecated
        self.id_ = int_attr(tweet, 'id')
        self.in_reply_to_screen_name = int_attr(tweet, 'in_reply_to_screen_name')
        self.in_reply_to_status_id = int_attr(tweet, 'in_reply_to_status_id')
        self.in_reply_to_user_id = int_attr(tweet, 'in_reply_to_user_id')
        self.lang = str_attr(tweet, 'lang')
        self.place = obj_attr(tweet, 'place', Place)
        self.possibly_sensitive = bool_attr(tweet, 'possibly_sensitive')
        self.quoted_status_id = int_attr(tweet, 'quoted_status_id')
        self.quoted_status = obj_attr(tweet, 'quoted_status', type(self))
        self.scopes = dict_attr(tweet, 'scopes')
        self.retweet_count = int_attr(tweet, 'retweet_count')
        self.retweeted = bool_attr(tweet, 'retweeted')
        self.retweeted_status = obj_attr(tweet, 'retweeted_status', type(self))
        self.source = str_attr(tweet, 'source')
        self.text = str_attr(tweet, 'text')
        self.truncated = bool_attr(tweet, 'truncated')
        self.user = obj_attr(tweet, 'user', User)


