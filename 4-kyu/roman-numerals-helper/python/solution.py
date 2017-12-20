class RomanNumerals:
    """
    I will just blend my two independent solutions 
    to the Roman Encoder/Decoder katas here.    
    """ 
    @classmethod
    def to_roman(cls, n):
        conversion = {1000: "M", 900: "CM", 500: "D",
			          400: "CD", 100: "C", 90: "XC", 
			          50: "L", 40: "XL", 10: "X",
			          9: 'IX', 5: "V", 4: "IV", 1: "I"}
        res = ''
        for key in sorted(conversion, reverse=True):
		    q, r = divmod(n, key)
		    if q == 0:
			    continue
		    else:
			    res += q * conversion[key]
			    n = r
			    if n == 0: break
        return res
        
    @classmethod
    def from_roman(cls, n):
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M" : 1000}
        idx = res = 0
        while idx < len(n):
            x = mapping[n[idx]]
            try:
                y = mapping[n[idx + 1]] 
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