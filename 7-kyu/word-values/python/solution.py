def nameValue(myList):
    return [(i+1) * sum(max(0, ord(n)-96) for n in w) for i, w in enumerate(myList)]