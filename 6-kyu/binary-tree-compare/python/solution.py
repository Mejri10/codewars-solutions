def compare(a, b):       
    if (a is None) or (b is None):
        return a == b
    else:
        return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right)