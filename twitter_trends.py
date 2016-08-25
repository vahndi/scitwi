from pandas import DataFrame
from twitter.api import TwitterListResponse



class TwitterTrends(object):

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
        
        return self._response_dict['locations']
        

    @property
    def trends_list(self):
        
        return self._response_dict['trends']
        
    @property
    def trends_dataframe(self):
        
        return DataFrame(self.trends_list)
