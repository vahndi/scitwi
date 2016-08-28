from scitwi.entities.entities import Entities
from scitwi.places.geo import Geo
from scitwi.places.place import Place
from scitwi.places.tweet_coordinates import TweetCoordinates
from scitwi.tweets.contributor import Contributor
from scitwi.tweets.current_user_retweet import CurrentUserRetweet
from scitwi.users.user import User
from scitwi.utils.attrs import list_obj_attr, obj_attr, datetime_attr, int_attr, bool_attr, str_attr, dict_attr, \
    list_str_attr
from scitwi.utils.strs import attr_string, list_attr_string


class Tweet(object):
    """
    https://dev.twitter.com/overview/api/tweets
    """
    def __init__(self, tweet: dict):

        self.contributors = list_obj_attr(tweet, 'contributors', Contributor)
        self.coordinates = obj_attr(tweet, 'coordinates', TweetCoordinates)
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
        self.withheld_copyright = bool_attr(tweet, 'withheld_copyright')
        self.withheld_in_countries = list_str_attr(tweet, 'withheld_in_countries')
        self.withheld_scope = str_attr(tweet, 'withheld_scope')

    def __str__(self):

        str_out = ''
        str_out += list_attr_string('Contributors', self.contributors)
        str_out += attr_string('Coordinates', self.coordinates)
        str_out += attr_string('Created At', self.created_at)
        str_out += attr_string('Current User Retweet', self.current_user_retweet)
        str_out += attr_string('Entities', self.entities)
        str_out += attr_string('Favorite Count', self.favorite_count)
        str_out += attr_string('Favorited', self.favorited)
        str_out += attr_string('Filter Level', self.filter_level)
        str_out += attr_string('Id', self.id_)
        str_out += attr_string('In Reply To Screen Name', self.in_reply_to_screen_name)
        str_out += attr_string('In Reply To Status Id', self.in_reply_to_status_id)
        str_out += attr_string('Lang', self.lang)
        str_out += attr_string('Place', self.place)
        str_out += attr_string('Possibly Sensitive', self.possibly_sensitive)
        str_out += attr_string('Quoted Status Id', self.quoted_status_id)
        str_out += attr_string('Quoted Status', self.quoted_status)
        str_out += attr_string('Scopes', self.scopes)
        str_out += attr_string('Retweet Count', self.retweet_count)
        str_out += attr_string('Retweeted', self.retweeted)
        str_out += attr_string('Retweeted Status', self.retweeted_status)
        str_out += attr_string('Source', self.source)
        str_out += attr_string('Text', self.text)
        str_out += attr_string('Truncated', self.truncated)
        str_out += attr_string('User', self.user)
        str_out += attr_string('Withheld Copyright', self.withheld_copyright)
        str_out += list_attr_string('Withheld In Countries', self.withheld_in_countries)
        str_out += attr_string('Withheld Scope', self.withheld_scope)
        return str_out
