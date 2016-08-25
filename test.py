from ApiKeys.twitter import (
    CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
)
from twypy.places import TwitterApp
from places import PlacesWOE



app = TwitterApp()
trends = app.get_trends(PlacesWOE.UnitedKingdom)
print(trends.as_of)
print(trends.created_at)
print(trends.locations)