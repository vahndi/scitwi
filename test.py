from api_keys.twitter import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from scitwi.places import PlaceWOE
from scitwi.twitter_app import TwitterApp
from scitwi.trends import Trends
from pprint import pprint
from scitwi.search.search_query import SearchQuery

app = TwitterApp(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                 oauth_token=OAUTH_TOKEN, oauth_token_secret=OAUTH_TOKEN_SECRET)


def test_trends():

    trends_uk = app.get_trends(PlaceWOE.USA)
    print(trends_uk)
    for trend in trends_uk.trends_list:
        print(trend)


def test_common_trends():

    trends_uk = app.get_trends(PlaceWOE.UK)
    trends_us = app.get_trends(PlaceWOE.USA)
    print(trends_uk.trend_names)
    print(trends_us.trend_names)
    print(Trends.common_trend_names(trends_uk, trends_us))


def test_search():

    q = '#superbowl'
    results = app.search_tweets(q, 100)
    print(type(results))
    print(results)


def test_query():

    q = SearchQuery(from_account='realDonaldTrump')
    results = app.search_tweets(query=q)
    for s in results.statuses:
        print(s)


if __name__ == '__main__':

    # test_trends()
    test_search()
    # test_query()
