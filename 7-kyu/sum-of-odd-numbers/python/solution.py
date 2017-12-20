def row_sum_odd_numbers(n):
    k = 1 + (n + 2)*(n - 1)    
    return sum(k-2*i for i in range(n)) 
    
    	