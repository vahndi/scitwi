from scitwi.utils import int_attr, str_attr, attr_string


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
        str_out += attr_string('Height', self.height)
        str_out += attr_string('Width', self.width)
        str_out += attr_string('Resize', self.resize)

        return str_out
