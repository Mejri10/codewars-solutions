def isomorph(a, b):
    if len(set(a)) != len(set(b)):
        return False

    mapping = dict(zip(a, b))
    for letterA, letterB in zip(a, b):
        if mapping[letterA] != letterB:
            return False
    return True