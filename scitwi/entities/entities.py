from scitwi.entities.hash_tag import HashTag
from scitwi.media.media_item import MediaItem


class Entities(object):

    def __init__(self, entities: dict):

        self.hashtags = [HashTag(h) for h in entities['hashtags']]
        self.media = ([MediaItem(m) for m in entities['media']]
                      if 'media' in entities.keys() else None)
        self.symbols = entities['symbols']
        self.urls = entities['urls']
        self.user_mentions = entities['user_mentions']

