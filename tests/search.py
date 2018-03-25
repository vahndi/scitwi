from scitwi.search.search_query import SearchQuery
from tests.shared import app


def test_search_string():

    q = '#superbowl'
    results = app.search_tweets(q, 100)
    print(results)


def test_from_account():

    q = SearchQuery(from_account='realDonaldTrump')
    results = app.search_tweets(query=q)
    for s in results.statuses:
        print(s)


def test_hashtag():

    q = SearchQuery(hashtags='#halftimeshow')
    results = app.search_tweets(query=q)
    for s in results.statuses:
        print(s)


def test_response():

    q = SearchQuery(hashtags='#halftimeshow')
    results = app.search_tweets(query=q)
    print(results)


if __name__ == '__main__':

    test_search_string()
    # test_from_account()
    # test_hashtag()
    # test_response()
