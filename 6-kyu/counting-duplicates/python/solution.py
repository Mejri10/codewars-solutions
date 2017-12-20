from collections import Counter

def duplicate_count(text):
    return len(filter(lambda x: x[1] > 1, Counter(text.lower()).items()))
     
     

