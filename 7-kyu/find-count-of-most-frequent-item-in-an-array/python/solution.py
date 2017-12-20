def most_frequent_item_count(collection):
    count = {}
    for n in collection:
        count[n] = count.get(n, 0) + 1
    return 0 if not collection else sorted(count.values())[-1]