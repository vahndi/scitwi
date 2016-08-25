from ApiKeys.twitter import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from scitwi import PlacesWOE, TwitterApp

app = TwitterApp(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                 oauth_token=OAUTH_TOKEN, oauth_token_secret=OAUTH_TOKEN_SECRET)

trends = app.get_trends(PlacesWOE.UnitedKingdom)
for t in trends.trends_list:
    print(t)
