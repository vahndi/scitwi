def listify(obj):

    if obj is None:
        return []
    elif type(obj) is list:
        return obj
    elif type(obj) is tuple:
        return list(obj)
    else:
        return [obj]
