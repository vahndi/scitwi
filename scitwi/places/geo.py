from scitwi.utils import attr_string


class Geo(object):

    def __init__(self, geo: dict):

        self.type_ = geo['type']
        self.coordinates = geo['coordinates']

    def __str__(self):

        str_out = ''
        str_out += attr_string('Type', self.type_)
        str_out += attr_string('Coordinates', self.coordinates)
        return str_out
