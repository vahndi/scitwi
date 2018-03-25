from scitwi.media.sizes import Sizes
from scitwi.utils.attrs import str_attr, int_attr, list_int_attr, obj_attr
from scitwi.utils.strs import obj_string, list_obj_string


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
        str_out += obj_string('Display Url', self.display_url)
        str_out += obj_string('Expanded Url', self.expanded_url)
        str_out += obj_string('Id', self.id_)
        str_out += list_obj_string('Indices', self.indices)
        str_out += obj_string('Media Url', self.media_url)
        str_out += obj_string('Media Url Https', self.media_url_https)
        str_out += obj_string('Sizes', self.sizes)
        str_out += obj_string('Source Status Id', self.source_status_id)
        str_out += obj_string('Type', self.type_)
        str_out += obj_string('Url', self.url)

        return str_out
