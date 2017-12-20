def square_it(digits):
    s = str(digits)
    sqrt = len(s)**.5
    return "Not a perfect square!" if not sqrt.is_integer() else '\n'.join(s[i*int(sqrt): (i+1)*int(sqrt)] for i in range(int(sqrt)))