from scitwi.media.media_item import MediaItem


class ExtendedEntities(object):

    def __init__(self, entities: dict):

        self.media = (
            [MediaItem(m) for m in entities['media']]
            if 'media' in entities.keys()
            else []
        )

    def __str__(self):

        str_out = 'EXTENDED ENTITIES\n'
        str_out += '-----------------\n\n'
        if self.media:
            str_out += 'Media:\n'
            for media_item in self.media:
                str_out += '\t%s\n' % str(media_item)

        return str_out
