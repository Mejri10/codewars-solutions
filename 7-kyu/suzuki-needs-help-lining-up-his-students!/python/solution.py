def lineup_students(string):
    return sorted(sorted(string.split(),reverse=True),key=len,reverse=True)