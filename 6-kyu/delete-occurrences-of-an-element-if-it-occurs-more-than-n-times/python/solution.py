from collections import Counter

def delete_nth(order, max_e):
    order = order[::-1]
    counts = Counter(order)
    for n in set(order):
        if counts[n] > max_e:
            for _ in range(counts[n] - max_e):
                order.remove(n)
    return order[::-1]