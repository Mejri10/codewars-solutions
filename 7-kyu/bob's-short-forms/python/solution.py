def short_form(s):
    vowels = 'aeiouAEIOU'
    return s if len(s) < 3 else s[0] + filter(lambda x: x not in vowels, s[1:-1]) + s[-1] 
        
        