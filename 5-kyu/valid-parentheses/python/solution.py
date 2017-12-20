def valid_parentheses(s):
    open = 0
    for c in s.strip():
        if c == '(': open += 1
        if c == ')': open -= 1
        if open < 0: break
    return True if open == 0 else False