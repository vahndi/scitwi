from typing import List

from scitwi.entities.hashtag import Hashtag
from scitwi.media.media_item import MediaItem
from scitwi.users.user_mention import UserMention
from scitwi.utils import list_obj_attr, list_str_attr


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
        if self.hashtags:
            str_out += 'Hashtags:\n'
            for hashtag in self.hashtags:
                str_out += '\t%s\n' % str(hashtag)
        if self.media:
            str_out += 'Media:\n'
            for media_item in self.media:
                str_out += '\t%s\n' % str(media_item)
        if self.symbols:
            str_out += 'Symbols:\n'
            for symbol in self.symbols:
                str_out += '\t%s\n' % str(symbol)
        if self.user_mentions:
            str_out += 'User Mentions:'
            for mention in self.user_mentions:
                str_out += '\t%s\n' % str(mention)

        return str_out
