from pandas import DataFrame
from twitter.api import TwitterListResponse
from .trend import Trend


class Trends(object):

    def __init__(self, response: TwitterListResponse):
        
        self._response = response
    
    @property
    def _response_dict(self):
        
        return self._response[0]

    @property
    def as_of(self):
        
        return self._response_dict['as_of']

    @property
    def created_at(self):
        
        return self._response_dict['created_at']

    @property
    def locations(self):
        
        return self._response_dict['places']

    @property
    def trends_list(self):
        
        return [Trend(trend_dict=t, as_of=self.as_of,
                      created_at=self.created_at, locations=self.locations)
                for t in self._response_dict['trends']]
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
