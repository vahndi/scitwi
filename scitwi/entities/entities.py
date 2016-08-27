from typing import List

from scitwi.entities.hashtag import Hashtag
from scitwi.media.media_item import MediaItem
from scitwi.users.user_mention import UserMention


class Entities(object):
    """
    https://dev.twitter.com/overview/api/entities
    """
    def __init__(self, entities: dict):

        self.hashtags = (
            [Hashtag(h) for h in entities['hashtags']]
            if 'hashtags' in entities.keys()
            else []
        )  # type: List[Hashtag]
        self.media = (
            [MediaItem(m) for m in entities['media']]
            if 'media' in entities.keys() else []
        )  # type: List[MediaItem]
        self.symbols = (
            entities['symbols'] if 'symbols' in entities.keys() else []
        )  # type: List[str]
        self.urls = (
            entities['urls'] if 'urls' in entities.keys() else []
        )  # type: List[str]
        self.user_mentions = (
            [UserMention(m) for m in entities['user_mentions']]
            if 'user_mentions' in entities.keys()
            else []
        )  # type: List[UserMention]

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
