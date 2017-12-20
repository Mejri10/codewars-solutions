from string import ascii_lowercase as letters

def decode(code, key):
    translate = dict(zip(range(1, 27), letters))
    key_nums = str(key) * (len(code)//len(str(key)) + 1)
    msg = [code[k] - int(key_nums[k]) for k in range(len(code))]
    return ''.join([translate[num] for num in msg])