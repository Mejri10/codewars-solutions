def dating_range(age):
    if age > 14:
        return "{}-{}".format(int(age/2 + 7), int((age - 7) * 2))
    else:
        return "{}-{}".format(int(age - 0.1*age), int(age + 0.1*age))