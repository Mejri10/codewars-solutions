from operator import itemgetter

def kill_count(counselors, jason):
    return map(itemgetter(0), filter(lambda x: x[1] < jason, counselors))