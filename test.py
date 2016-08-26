from ApiKeys.twitter import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from scitwi import PlacesWOE, TwitterApp, TwitterTrends

app = TwitterApp(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                 oauth_token=OAUTH_TOKEN, oauth_token_secret=OAUTH_TOKEN_SECRET)

trends_UK = app.get_trends(PlacesWOE.UnitedKingdom)
trends_US = app.get_trends(PlacesWOE.UnitedStates)
print(trends_UK.trend_names)
print(trends_US.trend_names)
print(TwitterTrends.common_trend_names(trends_UK, trends_US))
