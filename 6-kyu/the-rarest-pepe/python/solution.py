from collections import Counter

def find_rarest_pepe(pepes):
    res = []
    pepes = Counter(pepes).most_common()
    min_freq = min(pepes, key = lambda x: x[1])[1]
    if min_freq >= 5: 
        return 'No rare pepes!'
    else:
        for pepe, freq in pepes:
            if freq == min_freq:
                res.append(pepe)
    return sorted(res) if len(res) > 1 else res[0]
        
        