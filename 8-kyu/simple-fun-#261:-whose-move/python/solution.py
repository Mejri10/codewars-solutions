def whoseMove(lastPlayer, win):
    return ('black', 'white')[(lastPlayer=='white'and win) or (lastPlayer=='black' and not win)]