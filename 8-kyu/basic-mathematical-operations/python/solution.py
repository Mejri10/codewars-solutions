def basic_op(operator, value1, value2):
    op = ["+", "-", "*", "/"]
    return [value1 + value2, value1 - value2, value1 * value2, value1 / value2][op.index(operator)]