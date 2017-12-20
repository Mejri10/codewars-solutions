def rps(p1, p2):
    beat = {"scissors": "rock", "paper": "scissors", "rock": "paper"}            
    if beat[p1] == p2:
        return "Player 2 won!"
    elif beat[p2] == p1:
        return "Player 1 won!"
    else: 
        return "Draw!"