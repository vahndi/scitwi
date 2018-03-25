from scitwi.utils.attrs import list_float_attr, str_attr
from scitwi.utils.strs import list_obj_string, obj_string


class TweetCoordinates(object):
    """
    https://dev.twitter.com/overview/api/tweets#obj-coordinates
    """
    def __init__(self, coordinates: dict):

        self.coordinates = list_float_attr(coordinates, 'coordinates')
        self.type_ = str_attr(coordinates, 'type')

    def __str__(self):

        str_out = ''
        str_out += list_obj_string('Coordinates', self.coordinates)
        str_out += obj_string('Type', self.type_)
        return str_out

