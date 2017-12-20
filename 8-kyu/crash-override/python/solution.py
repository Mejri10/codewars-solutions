def alias_gen(f_name, l_name):
    try:
        return '{} {}'.format(FIRST_NAME[f_name[0].upper()], SURNAME[l_name[0].upper()])     
    except KeyError:
        return 'Your name must start with a letter from A - Z.'