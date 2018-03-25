from scitwi.media.size import Size
from scitwi.utils.attrs import obj_attr
from scitwi.utils.strs import obj_string


class Sizes(object):
    """
    https://dev.twitter.com/overview/api/entities#obj-sizes
    """
    def __init__(self, sizes: dict):

        self.large = obj_attr(sizes, 'large', Size)  # type: Size
        self.medium = obj_attr(sizes, 'medium', Size)  # type: Size
        self.small = obj_attr(sizes, 'small', Size)  # type: Size
        self.thumb = obj_attr(sizes, 'thumb', Size)  # type: Size

    def __str__(self):

        str_out = ''
        str_out += obj_string('Large', self.large)
        str_out += obj_string('Medium', self.medium)
        str_out += obj_string('Small', self.small)
        str_out += obj_string('Thumb', self.thumb)

        return str_out
