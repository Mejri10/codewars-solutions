import re

def trump_detector(trump_speech):
    duplicates_regex = re.compile(r"([aeiou])\1+", re.IGNORECASE)
    duplicates = []
    normal_speech = re.sub(duplicates_regex, lambda x: duplicates.append(x.group()) or x.group()[0], trump_speech)
    extra_vowels = sum(len(d)-1 for d in duplicates)
    total_vowels = sum(1 for c in normal_speech if c.lower() in "aeiou")
    return round(extra_vowels/total_vowels, 2)