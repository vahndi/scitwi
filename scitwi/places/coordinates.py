from scitwi.utils.strs import attr_string


class Coordinates(object):

    def __init__(self, coordinates: dict):

        self.coordinates = coordinates['coordinates']

    def __str__(self):

        return attr_string('Coordinates', self.coordinates)

