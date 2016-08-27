from scitwi.utils import int_attr, str_attr


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
        if self.height:
            str_out += 'Height: %i\n' % self.height
        if self.width:
            str_out += 'Width: %i\n' % self.width
        if self.resize:
            str_out += 'Resize: %s' % self.resize

        return str_out
