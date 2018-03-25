from scitwi.utils.attrs import int_attr, str_attr
from scitwi.utils.strs import obj_string


class Size(object):
    """
    https://dev.twitter.com/overview/api/entities#obj-size
    """
    def __init__(self, size: dict):

        self.height = int_attr(size, 'h')
        self.width = int_attr(size, 'w')
        self.resize = str_attr(size, 'resize')

    def __str__(self):

        str_out = ''
        str_out += obj_string('Height', self.height)
        str_out += obj_string('Width', self.width)
        str_out += obj_string('Resize', self.resize)

        return str_out
