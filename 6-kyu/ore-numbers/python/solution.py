def find_divs(n):
    divs = []
    for i in range(1, n+1):
        if n % i == 0:
            divs.append(i)
    return divs
    
def harmonic_mean(arr):
    return len(arr)/sum(1.0/n for n in arr)
    
def is_integer(n):
    tol = 1e-6  # arbitrarily chosen
    return abs(int(n) - n) < tol   

def is_ore(n):
    return is_integer(harmonic_mean(find_divs(n)))
    