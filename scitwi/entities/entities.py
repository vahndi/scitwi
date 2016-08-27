from typing import List

from scitwi.entities.hashtag import Hashtag
from scitwi.media.media_item import MediaItem
from scitwi.users.user_mention import UserMention
from scitwi.utils import list_obj_attr, list_str_attr, attr_string, list_attr_string


class Entities(object):
    """
    https://dev.twitter.com/overview/api/entities
    """
    def __init__(self, entities: dict):

        self.hashtags = list_obj_attr(entities, 'hashtags', Hashtag)  # type: List[Hashtag]
        self.media = list_obj_attr(entities, 'media', MediaItem)  # type: List[MediaItem]
        self.symbols = list_str_attr(entities, 'symbols')
        self.urls = list_str_attr(entities, 'urls')
        self.user_mentions = list_obj_attr(entities, 'user_mentions', UserMention)  # type: List[UserMention]

    def __str__(self):

        str_out = ''
        str_out += attr_string('Hashtags', self.hashtags)
        str_out += list_attr_string('Media', self.media)
        str_out += attr_string('Symbols', self.symbols)
        str_out += list_attr_string('User Mentions', self.user_mentions)
        return str_out
