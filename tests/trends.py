from scitwi.places import PlaceWOE
from scitwi.trends import Trends
from tests.shared import app


def test_trends():

    trends_uk = app.get_trends(PlaceWOE.USA)
    print('UK trend names:\n', trends_uk, '\n')
    print('UK trend details:\n')
    for trend in trends_uk.trends_list:
        print(trend)
    print('\n')


def test_common_trends():

    trends_uk = app.get_trends(PlaceWOE.UK)
    trends_us = app.get_trends(PlaceWOE.USA)
    print('UK trend names:\n', trends_uk.trend_names, '\n')
    print('US trend names:\n', trends_us.trend_names, '\n')
    print('Common trend names:\n', Trends.common_trend_names(trends_uk, trends_us), '\n')
    print('\n')


if __name__ == '__main__':

    test_trends()
    test_common_trends()
