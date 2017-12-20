def calc(expr):
    operators = {"+": lambda x,y: x + y,
                 "-": lambda x,y: x - y,
                 "*": lambda x,y: x * y,
                 "/": lambda x,y: x / y}
    args = expr.split()
    stack = [0]
    for arg in args:
        if arg not in operators.keys():
            stack.append(float(arg))
        else:
            y, x = stack.pop(), stack.pop()
            stack.append(operators[arg](x, y))            
    return stack[-1]