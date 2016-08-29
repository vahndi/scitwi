def attr_string(attr_name: str, attr_value):

    if attr_value:
        return '%s: %s\n' % (attr_name, str(attr_value))
    return ''


def list_attr_string(attr_name: str, attr_values):

    str_out = ''
    print(attr_name, attr_values)
    if attr_values:
        str_out += '%s:\n' % attr_name
        for v in attr_values:
            str_out += '\t%s\n' % str(v)
    return str_out
