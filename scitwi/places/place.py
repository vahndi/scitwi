from scitwi.places.bounding_box import BoundingBox
from scitwi.utils.attrs import dict_attr, str_attr
from scitwi.utils.strs import obj_string


class Place(object):
    """
    https://dev.twitter.com/overview/api/places
    """
    def __init__(self, place: dict):

        self.attributes = dict_attr(place, 'attributes')
        self.bounding_box = BoundingBox(place['bounding_box'])
        self.contained_within = place['contained_within']
        self.country = place['country']
        self.country_code = place['country_code']
        self.full_name = place['full_name']
        self.id_ = place['id']
        self.name = place['name']
        self.place_type = place['place_type']
        self.url = place['url']

        # may or may not exist:
        self.street_address = str_attr(place, 'street_address')
        self.locality = str_attr(place, 'locality')
        self.region = str_attr(place, 'region')
        self.iso3 = str_attr(place, 'iso3')
        self.postal_code = str_attr(place, 'postal_code')
        self.phone = str_attr(place, 'phone')
        self.twitter = str_attr(place, 'twitter')
        self.url = str_attr(place, 'url')
        self.app_id = str_attr(place, 'app:id') # TODO: this could also be a list of str

    def __str__(self):

        str_out = ''

        str_out += obj_string('Attributes', self.attributes)
        str_out += obj_string('Bounding Box', self.bounding_box)
        str_out += obj_string('Contained Within', self.contained_within)
        str_out += obj_string('Country', self.country)
        str_out += obj_string('Country Code', self.country_code)
        str_out += obj_string('Full Name', self.full_name)
        str_out += obj_string('Id', self.id_)
        str_out += obj_string('Name', self.name)
        str_out += obj_string('Place Type', self.place_type)
        str_out += obj_string('Street Address', self.street_address)
        str_out += obj_string('Locality', self.locality)
        str_out += obj_string('Region', self.region)
        str_out += obj_string('ISO 3', self.iso3)
        str_out += obj_string('Postal Code', self.postal_code)
        str_out += obj_string('Phone', self.phone)
        str_out += obj_string('Twitter', self.twitter)
        str_out += obj_string('Url', self.url)
        str_out += obj_string('App Id', self.app_id)

        return str_out
