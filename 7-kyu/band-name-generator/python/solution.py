def band_name_generator(name):
    return name.title() + name[1:] if name.endswith(name[0]) else "The {}".format(name.title())