def to_query_string(data):
    res = []
    for k, v in sorted(data.items()):
        if isinstance(v, list):
            for vs in v:
                res.append("{}={}".format(k, vs))
        else:
            res.append("{}={}".format(k, v))
    return "&".join(res)
        