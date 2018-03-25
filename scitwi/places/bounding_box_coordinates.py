from scitwi.utils.strs import obj_string


class BoundingBoxCoordinates(object):

    def __init__(self, coordinates: list):

        self.coordinates = coordinates

    def __str__(self):

        return obj_string('Coordinates', self.coordinates)

