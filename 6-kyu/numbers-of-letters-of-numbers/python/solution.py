digitsName = ["zero", "one", "two", "three","four",
              "five", "six", "seven", "eight", "nine"]
              
def digits_to_name(n):
    return ''.join(digitsName[int(d)] for d in str(n))

def numbers_of_letters(n):                 
    res = []
    nName = digits_to_name(n)
    while n != len(nName):
        res.append(nName)
        n = len(nName)
        nName = digits_to_name(n)
    else:
        res.append(nName)
    return res