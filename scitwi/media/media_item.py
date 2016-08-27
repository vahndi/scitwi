from scitwi.media.sizes import Sizes
from scitwi.utils import str_attr, int_attr, list_int_attr, obj_attr


class MediaItem(object):
    """
    https://dev.twitter.com/overview/api/entities#obj-media
    """
    def __init__(self, media: dict):

        self.display_url = str_attr(media, 'display_url')
        self.expanded_url = str_attr(media, 'expanded_url')
        self.id_ = int_attr(media, 'id')
        self.indices = list_int_attr(media, 'indices')
        self.media_url = str_attr(media, 'media_url')
        self.media_url_https = str_attr(media, 'media_url_https')
        self.sizes = obj_attr(media, 'sizes', Sizes)  # type: Sizes
        self.source_status_id = int_attr(media, 'source_status_id')
        self.type_ = str_attr(media, 'type')
        self.url = str_attr(media, 'url')

    def __str__(self):

        str_out = ''
        if self.display_url:
            str_out += 'Display Url: %s\n' % self.display_url
        if self.expanded_url:
            str_out += 'Expanded Url: %s\n' % self.expanded_url
        if self.id_:
            str_out += 'Id: %i\n' % self.id_
        if self.indices:
            str_out += 'Indices: %s\n' % str(self.indices)
        if self.media_url:
            str_out += 'Media Url: %s \n' % self.media_url
        if self.media_url_https:
            str_out += 'Media Url Https: %s \n' % self.media_url_https
        if self.sizes:
            str_out += 'Sizes: %s\n' % str(self.sizes)
        if self.source_status_id:
            str_out += 'Source Status Id: %i\n' % self.source_status_id
        if self.type_:
            str_out += 'Type: %s\n' % self.type_
        if self.url:
            str_out += 'Url: %s\n' % self.url

        return str_out
