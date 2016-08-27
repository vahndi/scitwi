from scitwi.media.media_item import MediaItem


class ExtendedEntities(object):

    def __init__(self, entities: dict):

        self.media = [MediaItem(m) for m in entities['media']]

