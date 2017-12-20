def countWins(winnerList, country):
    return sum(1 for season in winnerList if season['country'] == country)