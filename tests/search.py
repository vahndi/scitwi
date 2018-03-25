from scitwi.search.search_query import SearchQuery
from tests.shared import app
from pickle import dump, load, loads


def test_search_string():

    q = '#superbowl'
    results = app.search_tweets(query=q)
    print(results)


def test_from_account():

    q = SearchQuery(from_account='realDonaldTrump')
    results = app.search_tweets(query=q)
    print(results)


def test_hashtag():

    q = SearchQuery(hashtags='#halftimeshow')
    results = app.search_tweets(query=q)
    print(results)


def test_response():

    q = SearchQuery(hashtags='#halftimeshow')
    results = app.search_tweets(query=q)
    print(results)


def test_long_call():

    q = SearchQuery(hashtags='blm')
    results = app.search_tweets(query=q, count=200)
    dump(results, open('./results.pkl', 'wb'))
    print(results)


def read_results():

    results = load(open('./results.pkl', 'rb'))
    print(results.statuses[99])
    print(results.statuses[100])


if __name__ == '__main__':

    # test_search_string()
    # test_from_account()
    # test_hashtag()
    # test_response()
    test_long_call()
    read_results()
