def billboard(name, price=30):
    return reduce(lambda x,y: x + y, [price for i in range(len(name))])