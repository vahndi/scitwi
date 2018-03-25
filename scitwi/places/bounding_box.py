from scitwi.places.bounding_box_coordinates import BoundingBoxCoordinates
from scitwi.utils.attrs import obj_attr, str_attr
from scitwi.utils.strs import obj_string


class BoundingBox(object):
    """
    https://dev.twitter.com/overview/api/places#obj-boundingbox
    """
    def __init__(self, bounding_box: dict):

        self.coordinates = obj_attr(bounding_box, 'coordinates', BoundingBoxCoordinates)
        self.type_ = str_attr(bounding_box, 'type')

    def __str__(self):

        str_out = ''
        str_out += obj_string('Coordinates', self.coordinates)
        str_out += obj_string('Type', self.type_)
        return str_out
