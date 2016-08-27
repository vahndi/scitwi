from scitwi.media.sizes import Sizes
from scitwi.utils import str_attr, int_attr, list_int_attr, obj_attr, attr_string, list_attr_string


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
        str_out += attr_string('Display Url', self.display_url)
        str_out += attr_string('Expanded Url', self.expanded_url)
        str_out += attr_string('Id', self.id_)
        str_out += list_attr_string('Indices', self.indices)
        str_out += attr_string('Media Url', self.media_url)
        str_out += attr_string('Media Url Https', self.media_url_https)
        str_out += attr_string('Sizes', self.sizes)
        str_out += attr_string('Source Status Id', self.source_status_id)
        str_out += attr_string('Type', self.type_)
        str_out += attr_string('Url', self.url)

        return str_out
