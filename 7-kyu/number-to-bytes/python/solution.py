def to_bin(n):
    return bin(n)[2:]

def to_bytes(n):
    octets = []
    while n > 0xff:
        octets.append(to_bin(n % 0x100).zfill(8))
        n /= 0x100
    else:
        octets.append(to_bin(n % 0x100).zfill(8))
    return octets[::-1]
        
    