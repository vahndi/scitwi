from pandas import DataFrame
from twitter.api import TwitterListResponse

from scitwi.places.location import Location
from scitwi.utils.attrs import datetime_attr, list_obj_attr
from scitwi.utils.strs import attr_string, list_attr_string
from .trend import Trend


class Trends(object):

    def __init__(self, response: TwitterListResponse):

        self._response = response
        self.as_of = datetime_attr(response[0], 'as_of')
        self.created_at = datetime_attr(response[0], 'created_at')
        self.locations = list_obj_attr(response[0], 'locations', Location)
        self.trends_list = [
            Trend(trend_dict=t, as_of=self.as_of,
                  created_at=self.created_at, locations=self.locations)
            for t in self._response_dict['trends']
        ]

    @property
    def _response_dict(self):
        
        return self._response[0]

    @property
    def trend_names(self):

        return [t.name for t in self.trends_list]
        
    @property
    def trends_dataframe(self):
        
        return DataFrame(self.trends_list)

    @staticmethod
    def common_trend_names(trends_1, trends_2):

        set_1 = set([trend.name for trend in trends_1.trends_list])
        set_2 = set([trend.name for trend in trends_2.trends_list])
        return sorted(set_1.intersection(set_2))

    def __str__(self):

        str_out = ''
        str_out += attr_string('As Of', self.as_of)
        str_out += attr_string('Created At', self.created_at)
        str_out += list_attr_string('Locations', self.locations)
        str_out += list_attr_string('Trends', self.trend_names)
        return str_out
