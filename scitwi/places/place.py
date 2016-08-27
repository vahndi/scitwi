from scitwi.places.bounding_box import BoundingBox


class Place(object):

    def __init__(self, place: dict):

        self.attributes = place['attributes']  # TODO: Find an example where attributes is not an empty dict
        self.bounding_box = BoundingBox(place['bounding_box'])
        self.contained_within = place['contained_within']
        self.country = place['country']
        self.country_code = place['country_code']
        self.full_name = place['full_name']
        self.id_ = place['id']
        self.name = place['name']
        self.place_type = place['place_type']
        self.url = place['url']
