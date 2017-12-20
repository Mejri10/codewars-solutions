def average_string(s):
    string2num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five':5,
                  'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num2string = {v:k for k,v in string2num.items()}    
    try:
        return num2string[int(sum(string2num[n] for n in s.split())/len(s.split()))]
    except (ZeroDivisionError, KeyError):
        return 'n/a'
