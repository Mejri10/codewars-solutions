from string import maketrans

def DNA_strand(dna):
    return dna.translate(maketrans('ATGC', 'TACG'))