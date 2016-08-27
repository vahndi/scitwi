from scitwi.entities.entities import Entities
from scitwi.locations.coordinates import Coordinates
from scitwi.locations.geo import Geo
from scitwi.locations.place import Place
from scitwi.status.status_metadata import StatusMetadata
from scitwi.utils import get_datetime


class Status(object):

    def __init__(self, status: dict):

        self.contributors = status['contributors']
        self.coordinates = (
            Coordinates(status['coordinates'])
            if 'coordinates' in status.keys() and status['coordinates'] is not None
            else None
        )
        self.created_at = get_datetime(status['created_at'])
        self.entities = (
            Entities(status['entities'])
            if 'entities' in status.keys() and status['entities'] is not None
            else None
        )
        self.extended_entities = (
            Entities(status['extended_entities'])
            if 'extended_entities' in status.keys() and status['extended_entities'] is not None
            else None
        )
        self.favorite_count = status['favorite_count']
        self.favorited = status['favorited']
        self.geo = (
            Geo(status['geo'])
            if 'geo' in status.keys() and status['geo'] is not None
            else None
        )
        self.id_ = status['id']
        self.id_str = status['id_str']
        self.in_reply_to_screen_name = status['in_reply_to_screen_name']
        self.in_reply_to_status_id = status['in_reply_to_status_id']
        self.in_reply_to_status_id_str = status['in_reply_to_status_id_str']
        self.in_reply_to_user_id = status['in_reply_to_user_id']
        self.in_reply_to_user_id_str = status['in_reply_to_user_id_str']
        self.is_quote_status = status['is_quote_status']
        self.lang = status['lang']
        self.metadata = (
            StatusMetadata(status['metadata']) if 'metadata' in status.keys() else None
        )
        self.place = (
            Place(status['place'])
            if 'place' in status.keys() and status['place'] is not None
            else None
        )
        self.possibly_sensitive = (
            status['possibly_sensitive'] if 'possibly_sensitive' in status.keys() else None
        )
        self.retweet_count = status['retweet_count']
        self.retweeted = status['retweeted']
        self.source = status['source']
        self.text = status['text']
        self.truncated = status['truncated']
