class BoundingBox(object):

    def __init__(self, bounding_box: dict):

        self.coordinates = bounding_box['coordinates']
        self.type_ = bounding_box['type']
