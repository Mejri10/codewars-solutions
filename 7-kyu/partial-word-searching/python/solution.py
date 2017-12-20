def word_search(query, seq):
    res = filter(lambda s: query.lower() in s.lower(), seq)
    return res if res else ["None"]
    