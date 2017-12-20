def zebulansNightmare(functionName):
    return ''.join([name.capitalize() if functionName.index(name) > 1 else name for name in functionName.split('_') ])