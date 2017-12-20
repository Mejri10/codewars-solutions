def share_price(invested, changes):
    return "{:.2f}".format(reduce(lambda x,y: x * (1 + y/100.0), [invested] + changes))