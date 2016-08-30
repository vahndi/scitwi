from datetime import datetime


def get_datetime(str_date: str):
    try:
        return datetime.strptime(str_date, '%a %b %d %H:%M:%S +0000 %Y')
    except:
        pass
    try:
        return datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%SZ')
    except:
        pass
    return None
