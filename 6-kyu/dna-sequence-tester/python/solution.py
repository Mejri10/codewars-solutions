from string import maketrans

def check_DNA(seq1, seq2):
    seq2 = seq2[::-1].translate(maketrans('ATCG','TAGC'))
    return seq1 in seq2 if len(seq2) >= len(seq1) else seq2 in seq1
    