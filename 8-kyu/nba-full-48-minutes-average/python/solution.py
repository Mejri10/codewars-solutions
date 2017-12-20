def nba_extrap(ppg, mpg):
    try:
        return round(48.0 * ppg/mpg, 1)
    except ZeroDivisionError:
        return 0