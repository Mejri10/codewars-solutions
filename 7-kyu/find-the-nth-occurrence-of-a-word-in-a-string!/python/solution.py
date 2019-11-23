def find_nth_occurrence(substring, string, occurrence=1):
    try:
        idx = -1
        for _ in range(occurrence):
            idx = string.index(substring, idx+1)
        return idx
    except ValueError:
        return -1
