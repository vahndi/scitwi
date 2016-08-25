from ApiKeys.twitter import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from scitwi import PlacesWOE, TwitterApp

app = TwitterApp(CONSUMER_KEY=CONSUMER_KEY, CONSUMER_SECRET=CONSUMER_SECRET,
                 OAUTH_TOKEN=OAUTH_TOKEN, OAUTH_TOKEN_SECRET=OAUTH_TOKEN_SECRET)
trends = app.get_trends(PlacesWOE.UnitedKingdom)
print(trends.as_of)
print(trends.created_at)
print(trends.locations)
print(trends.trends_dataframe)
