from datetime import datetime


def get_datetime(str_date):

    return datetime.strptime(str_date, '%a %b %d %H:%M:%S +0000 %Y')


