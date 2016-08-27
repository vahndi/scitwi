from scitwi.media.media_item_size import MediaItemSize


class MediaItemSizes(object):

    def __init__(self, sizes: dict):

        self.large = MediaItemSize(sizes['large'])
        self.medium = MediaItemSize(sizes['medium'])
        self.small = MediaItemSize(sizes['small'])
        self.thumb = MediaItemSize(sizes['thumb'])
