def mean(lst):
    numbers = [int(n) for n in lst if n.isdigit()]
    avg = round(sum(numbers)/float(len(numbers)),1)
    digits = ''.join(filter(lambda x: x.isalpha(), lst))
    
    return [avg, digits]
    