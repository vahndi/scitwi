from scitwi.media.size import Size
from scitwi.utils import obj_attr


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
        if self.large:
            str_out += 'Large: %s\n' % str(self.large)
        if self.medium:
            str_out += 'Large: %s\n' % str(self.large)
        if self.small:
            str_out += 'Large: %s\n' % str(self.large)
        if self.thumb:
            str_out += 'Large: %s\n' % str(self.large)

        return str_out
