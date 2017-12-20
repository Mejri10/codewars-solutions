def maskify(cc):
    if len(cc) > 3:
        return ''.join(len(cc[:-4])*'#' + cc[-4:])
    else:
        return cc