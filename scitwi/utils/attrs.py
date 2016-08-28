from scitwi.utils.misc import get_datetime


def bool_attr(attr_dict: dict, attr_dict_key: str):
    """
    :rtype: bool
    """
    if attr_dict_key in attr_dict.keys():
        return attr_dict[attr_dict_key]
    return None


def datetime_attr(attr_dict: dict, attr_dict_key: str):
    """
    :rtype: datetime
    """
    if attr_dict_key in attr_dict.keys():
        return get_datetime(attr_dict[attr_dict_key])
    return None


def dict_attr(attr_dict: dict, attr_dict_key: str):
    """
    :rtype: dict
    """
    if attr_dict_key in attr_dict.keys():
        return attr_dict[attr_dict_key]
    return {}


def int_attr(attr_dict: dict, attr_dict_key: str):
    """
    :rtype: int
    """
    if attr_dict_key in attr_dict.keys():
        return attr_dict[attr_dict_key]
    return None


def float_attr(attr_dict: dict, attr_dict_key: str):
    """
    :rtype: float
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

    if attr_dict_key in attr_dict.keys():
        return [obj_type(v) for v in attr_dict[attr_dict_key]]
    return []


def list_int_attr(attr_dict: dict, attr_dict_key: str):
    """
    :rtype: List[int]
    """
    if attr_dict_key in attr_dict.keys():
        return attr_dict[attr_dict_key]
    return []


def list_float_attr(attr_dict: dict, attr_dict_key: str):
    """
    :rtype: List[float]
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