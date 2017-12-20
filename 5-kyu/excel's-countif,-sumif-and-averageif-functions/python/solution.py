from operator import gt, ge, lt, le, eq, ne
import re

OPERATORS = {">": gt, ">=": ge, "<": lt, "<=": le, "<>": ne}
REGEX = re.compile(r"([<>=]+)([0-9\.]+)")

def count_if(values, criteria):
    if not isinstance(criteria, str):
        return values.count(criteria)
    else:
        if re.match(REGEX, criteria):
            operator, value = re.findall(REGEX, criteria)[0]
            return len(filter(lambda x: OPERATORS[operator](x, float(value)), values))
        else:
            return values.count(criteria)
    
def sum_if(values, criteria):
    if not isinstance(criteria, str):
        return criteria * values.count(criteria)
    else:
        operator, value = re.findall(REGEX, criteria)[0]
        return sum(filter(lambda x: OPERATORS[operator](x, float(value)), values))
    
def average_if(values,criteria):
    return float(sum_if(values, criteria))/count_if(values, criteria)