def areYouPlayingBanjo(name):
    return name + (' does not play banjo', ' plays banjo')[name.lower().startswith('r')]