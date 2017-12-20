def diamond(n):
    if n % 2 == 0 or n <= 0: 
        return None
    else:        
        sol = ''
        
        j = n/2 + 1
        for i in range(1, n+1, 2):
            sol += ((i * '*').rjust(j) + '\n')
            j += 1
        
        j = 1
        for i in range(n - 2, 0, -2):
            sol += ((i * '*').rjust(n-j) + '\n')
            j += 1
            
        return sol
        