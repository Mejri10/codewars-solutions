def numberAndIPaddress(s):
    print(s, type(s))
    if '.' in s:
        return str(int("".join(bin(int(i))[2:].zfill(8) for i in s.split('.')), 2))        
    else:
        return '.'.join([str(int(bin(int(s))[2:].zfill(32)[8*i:8*i+8], 2)) for i in range(4)])
        