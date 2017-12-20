import itertools

def permutation_average(n):
    digits = list(str(n))
    numbers = []
    
    for number in itertools.permutations(digits,len(digits)):
        number = int(''.join(number))
        if number not in numbers:
            numbers.append(number)

    return round(sum(numbers)/float(len(numbers)))
    
    
    
    