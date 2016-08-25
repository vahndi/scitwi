class TwitterTrend(object):

    def __init__(self, trend_dict, as_of, created_at, locations):

        self.as_of = as_of
        self.created_at = created_at
        self.locations = locations

        self.name = trend_dict['name']
        self.promoted_content = trend_dict['promoted_content']
        self.query = trend_dict['query']
        self.tweet_volume = trend_dict['tweet_volume']
        self.url = trend_dict['url']

    def __str__(self):

        return self.name
