from ApiKeys.twitter import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from scitwi import PlaceWOE, TwitterApp, Trends
from pprint import pprint


app = TwitterApp(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                 oauth_token=OAUTH_TOKEN, oauth_token_secret=OAUTH_TOKEN_SECRET)


def test_trends():

    trends_UK = app.get_trends(PlaceWOE.UnitedKingdom)
    trends_US = app.get_trends(PlaceWOE.UnitedStates)
    print(trends_UK.trend_names)
    print(trends_US.trend_names)
    print(Trends.common_trend_names(trends_UK, trends_US))


# test_trends()
q = '#NationalDogDay'
results = app.search_tweets(q, 100)
print(type(results))
pprint(results)



