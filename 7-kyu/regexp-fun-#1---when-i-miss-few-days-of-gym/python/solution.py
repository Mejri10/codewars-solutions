import re

def gym_slang(phrase):
    slangs = {"probably": "prolly", "i am": "i\'m", "instagram": "insta",
              "do not": "don't", "going to": "gonna",  "combination": "combo"}

    regex = re.compile("|".join(slangs.keys()), re.I)
    return re.sub(regex, lambda m: slangs[m.group(0)] if m.group(0)[0].islower() else slangs[m.group(0).lower()].capitalize(), phrase)