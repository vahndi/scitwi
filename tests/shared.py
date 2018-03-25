from api_keys.twitter import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from scitwi.twitter_app import TwitterApp

app = TwitterApp(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                 oauth_token=OAUTH_TOKEN, oauth_token_secret=OAUTH_TOKEN_SECRET)