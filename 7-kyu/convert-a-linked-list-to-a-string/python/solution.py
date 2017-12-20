def stringify(list):
    return "None" if list is None else "{} -> {}".format(list.data, stringify(list.next))