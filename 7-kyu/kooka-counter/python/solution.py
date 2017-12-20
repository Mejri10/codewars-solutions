import re

def kooka_counter(laughing):
    return len(re.findall(r"(?<=Ha)(ha)+|(?<=ha)(Ha)+", laughing)) + (1 if laughing else 0)