from datetime import datetime


def basic_attr(attr_dict: dict, attr_dict_key: str):
    if attr_dict_key in attr_dict.keys():
        return attr_dict[attr_dict_key]
    return None


def complex_attr(attr_dict: dict, attr_dict_key: str, complex_type: type):
    if attr_dict_key in attr_dict.keys():
        if attr_dict[attr_dict_key] is not None:
            return complex_type(attr_dict[attr_dict_key])
    return None


def get_datetime(str_date):

    return datetime.strptime(str_date, '%a %b %d %H:%M:%S +0000 %Y')