from datetime import datetime
from typing import List


def int_attr(attr_dict: dict, attr_dict_key: str):
    """
    :rtype: int
    """
    if attr_dict_key in attr_dict.keys():
        return attr_dict[attr_dict_key]
    return None


def str_attr(attr_dict: dict, attr_dict_key: str):
    """
    :rtype: str
    """
    if attr_dict_key in attr_dict.keys():
        return attr_dict[attr_dict_key]
    return ''


def list_obj_attr(attr_dict: dict, attr_dict_key: str, obj_type: type):

    if 'hashtags' in attr_dict.keys():
        return [obj_type(v) for v in attr_dict[attr_dict_key]]
    return []


def list_int_attr(attr_dict: dict, attr_dict_key: str):
    """
    :rtype: List[int]
    """
    if attr_dict_key in attr_dict.keys():
        return attr_dict[attr_dict_key]
    return []


def list_str_attr(attr_dict: dict, attr_dict_key: str):
    """
    :rtype: List[str]
    """
    if attr_dict_key in attr_dict.keys():
        return attr_dict[attr_dict_key]
    return []


def obj_attr(attr_dict: dict, attr_dict_key: str, obj_type: type):

    if attr_dict_key in attr_dict.keys():
        if attr_dict[attr_dict_key] is not None:
            return obj_type(attr_dict[attr_dict_key])
    return None


def get_datetime(str_date):

    return datetime.strptime(str_date, '%a %b %d %H:%M:%S +0000 %Y')