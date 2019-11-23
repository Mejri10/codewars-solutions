import re

def parse_example(example):
    expression, variable = example.split(" = ")
    return variable, "(" + expression + ")"

def only_one_variable_in_expression(expression):
    return len(set(select_variables(expression))) == 1
    
def select_variables(expression):
    return re.findall(r"[a-z]+", expression, flags=re.IGNORECASE)
    
def format_expression_for_eval(expression):
    expression = re.sub(r"(\d+)\s*\(", r"\1*(", expression)
    expression = re.sub(r"(\d)[a-z]", r"\1", expression, flags=re.IGNORECASE)
    expression = re.sub(r"[a-z]", r"1", expression)
    return expression

def simplify(examples, formula):
    while not only_one_variable_in_expression(formula):
        for example in examples:
            variable, expression = parse_example(example)
            formula = formula.replace(variable, expression)
    variable = select_variables(formula)[0]
    val = eval(format_expression_for_eval(formula))
    ans = "{}{}".format(val, variable)
    return ans if ans != "1c" else "1x"