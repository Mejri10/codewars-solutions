def help_zoom(key):
    return 'Yes' if (len(key)**.5).is_integer() and key == key[::-1] else 'No'