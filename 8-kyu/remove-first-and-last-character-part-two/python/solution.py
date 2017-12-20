def array(string):
    return None if len(string.split(',')) < 3 else ' '.join(string.split(',')[1:-1])