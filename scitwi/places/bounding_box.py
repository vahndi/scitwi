from scitwi.places.coordinates import Coordinates
from scitwi.utils import obj_attr, str_attr, attr_string


class BoundingBox(object):
    """
    https://dev.twitter.com/overview/api/places#obj-boundingbox
    """
    def __init__(self, bounding_box: dict):

        self.coordinates = obj_attr(bounding_box, 'coordinates', Coordinates)
        self.type_ = str_attr(bounding_box, 'type')

    def __str__(self):

        str_out = ''
        str_out += attr_string('Coordinates', self.coordinates)
        str_out += attr_string('Type', self.type_)
        return str_out
