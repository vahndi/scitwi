from datetime import datetime
from typing import List

from scitwi.places.location import Location
from scitwi.utils.strs import list_obj_string, obj_string


class Trend(object):

    def __init__(self, trend_dict: dict, as_of: datetime, created_at: datetime, locations: List[Location]):

        self.as_of = as_of
        self.created_at = created_at
        self.locations = locations

        self.name = trend_dict['name']
        self.promoted_content = trend_dict['promoted_content']
        self.query = trend_dict['query']
        self.tweet_volume = trend_dict['tweet_volume']
        self.url = trend_dict['url']

    def __str__(self):

        str_out = ''
        str_out += obj_string('Name', self.name)
        str_out += obj_string('Promoted Content', self.promoted_content)
        str_out += obj_string('Query', self.query)
        str_out += obj_string('Tweet Volume', self.tweet_volume)
        str_out += obj_string('Url', self.url)

        str_out += obj_string('As Of', self.url)
        str_out += obj_string('Created At', self.created_at)
        str_out += list_obj_string('Locations', self.locations)

        return str_out
