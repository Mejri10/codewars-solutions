def find_most_frequent(l):
    d = dict()
    for item in l:
        d[item] = d.get(item, 0) + 1     
    return set([key for key in d if d[key] == max(d.values())])