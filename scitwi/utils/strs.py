from datetime import datetime


def obj_string(obj_name: str, obj_value):
    """
    Return a string of attr_name:\n\tobj_value.attr_name[0]: obj_value.attr_value[0]...

    :param obj_name: The name of the object.
    :param obj_value: The value of the object.
    :return:
    """
    str_out = ''
    if obj_value:
        if type(obj_value) in (str, float, int, bool, datetime):
            return '%s: %s\n' % (obj_name, str(obj_value))
        else:
            str_out += '%s:\n' % obj_name
            str_out += '\n'.join(
                ['\t%s' % line for line in str(obj_value).split('\n')]
            )
            str_out += '\n'
    return str_out


def list_obj_string(attr_name: str, attr_values):
    """
    Return a string of "`attr_name`: `attr_value[0]`
                                     `attr_value[1]`..."

    :param attr_name: The name of the attribute.
    :param attr_values: The values of the attribute.
    :rtype: str
    """
    str_out = ''
    if attr_values:
        str_out += '%s:\n' % attr_name
        for v in attr_values:
            if type(v) in (str, float, int, bool, datetime):
                str_out += '\n'.join(
                    ['\t%s' % line for line in str(v).split('\n')]
                )
            else:
                str_out += '\t%s:\n' % type(v).__name__
                str_out += '\n'.join(
                    ['\t\t%s' % line for line in str(v).split('\n')]
                )
            str_out += '\n'
    return str_out
