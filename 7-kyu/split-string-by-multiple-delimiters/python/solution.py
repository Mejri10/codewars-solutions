def multiple_split(string, delimiters=[]):
    if not delimiters: return [string] if string else []
    ans = []
    temp = ''
    for letter in string:
        if letter not in delimiters: 
            temp += letter
        else:
            if temp: ans.append(temp)
            temp = ''   
    if temp: ans.append(temp)
    return ans