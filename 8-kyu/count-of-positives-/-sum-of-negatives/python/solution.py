def count_positives_sum_negatives(arr):
    return [sum(x > 0 for x in arr), sum(x for x in arr if x < 0)] if arr else arr