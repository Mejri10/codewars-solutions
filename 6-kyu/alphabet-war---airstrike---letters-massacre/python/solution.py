import re

def alphabet_war(fight):
    aftermatch = re.sub(r"\w{0,1}\*+\w{0,1}", "", fight)
    l = sum("sbpw".index(x)+1 for x in aftermatch if x in "sbpw")
    r = sum("zdqm".index(x)+1 for x in aftermatch if x in "zdqm")
    if l > r:
        return "Left side wins!"
    elif r > l:
        return "Right side wins!"
    else:
        return "Let's fight again!"