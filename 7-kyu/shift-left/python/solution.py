def shift_left(a, b):
    shortest, longest = sorted((a, b), key=len)
    for i in range(len(shortest)):
        substring = shortest[i:]
        if longest.endswith(substring):
            return i + (len(longest) - len(substring))
    return len(shortest) + len(longest)
        
    