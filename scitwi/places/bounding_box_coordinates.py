from scitwi.utils.strs import attr_string


class BoundingBoxCoordinates(object):

    def __init__(self, coordinates: list):

        self.coordinates = coordinates

    def __str__(self):

        return attr_string('Coordinates', self.coordinates)

