def likes(names):
    n = len(names)
    if n > 3:
        return "{0[0]}, {0[1]} and {1} others like this".format(names, n-2)
    elif n > 1:
        return "{} and {} like this".format(', '.join(names[:-1]), names[-1])
    elif n > 0:
        return "{[0]} likes this".format(names)
    else:
        return "no one likes this"
    