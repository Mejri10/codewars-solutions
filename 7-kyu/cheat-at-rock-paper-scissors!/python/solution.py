import random

def r_p_s_cheat(choice):
    beat = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
    if random.random() < 0.90:
        return beat[choice]
    else:
        return beat[beat[choice]]    