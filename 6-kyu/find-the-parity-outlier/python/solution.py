def find_outlier(integers):
    l = [i % 2 for i in integers]
    idx = l.index(1) if sum(l) == 1 else l.index(0)
    return integers[idx]
  