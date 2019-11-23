def find_missing(seq):
    return (seq[0] + seq[-1])*(len(seq)+1)/2 - sum(seq)
