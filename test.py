from ApiKeys.twitter import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from scitwi.places import PlaceWOE
from scitwi.twitter_app import TwitterApp
from scitwi.trends import Trends
from pprint import pprint
from datetime import datetime
from scitwi.search.search_query import SearchQuery

app = TwitterApp(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                 oauth_token=OAUTH_TOKEN, oauth_token_secret=OAUTH_TOKEN_SECRET)


def test_trends():

    trends_UK = app.get_trends(PlaceWOE.UnitedKingdom)
    trends_US = app.get_trends(PlaceWOE.UnitedStates)
    print(trends_UK.trend_names)
    print(trends_US.trend_names)
    print(Trends.common_trend_names(trends_UK, trends_US))


def test_search():

    q = '#NationalDogDay'
    results = app.search_tweets(q, 100)
    print(type(results))
    pprint(results)


def test_query():

    q = SearchQuery(all_of='hello world', any_of=['a', 'b', 'c'], none_of=['d', 'e', 'f'],
                    exact_phrase='goodbye cruel world', hashtags='boyakasha', language='en',
                    from_account='vahndi', to_account='susansung', mentioning_account='natwest',
                    from_date=datetime(2016,8,14), to_date=datetime(2016, 8, 21),
                    positive=True, negative=True, question=True, include_retweets=True)
    print(q)


# test_trends()
#test_search()
test_query()
