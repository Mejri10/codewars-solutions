def smallest_doll_size(largest_doll):
    if largest_doll() is None:
        return largest_doll.size
    else:
        return smallest_doll_size(largest_doll())