from scitwi.media.media_item_sizes import MediaItemSizes


class MediaItem(object):

    def __init__(self, media: dict):

        self.display_url = media['display_url']
        self.expanded_url = media['expanded_url']
        self.id_ = media['id']
        self.indices = media['indices']
        self.media_url = media['media_url']
        self.media_url_https = media['media_url_https']
        self.sizes = MediaItemSizes(media['sizes'])
        self.type_ = media['type']
