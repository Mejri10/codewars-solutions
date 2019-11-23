def case_sensitive(s):
    return [all(map(str.islower, s)), list(filter(str.isupper, s))]
    