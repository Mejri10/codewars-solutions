def find_E(s):
    if not s: return s
    n = list(s.lower()).count("e")
    return "{}".format(n) if n > 0 else "There is no \"e\"."
    