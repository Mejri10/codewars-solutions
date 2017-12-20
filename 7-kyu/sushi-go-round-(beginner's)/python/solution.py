def total_bill(s):
    return 2 * (list(s).count('r') - sum([i % 5 == 0 for i in range(1, list(s).count('r')+1)]))