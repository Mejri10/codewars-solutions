def solution(roman):
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M" : 1000}
    idx = res = 0
    while idx < len(roman):
        x = mapping[roman[idx]]
        try:
            y = mapping[roman[idx + 1]] 
            if y > x:
                res += (y - x)
                idx += 2
            else:
                res += x
                idx += 1         
        except IndexError:
            res += x
            idx += 1  
    return res