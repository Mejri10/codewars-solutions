from operator import *

def calculator(x,y,op):
    if not isinstance(op, str) or op not in "+-*/": return "unknown value"
    return {"+":add,"-":sub,"*":mul,"/":truediv}[op](x,y)