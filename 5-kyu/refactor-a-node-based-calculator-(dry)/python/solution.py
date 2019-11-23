import operator as o
class op:
  def __init__(self,a,b): self.a,self.b=a,b
  def compute(self): return getattr(o,self.__class__.__name__)(self.a,self.b)
class value(int): pass
class add(op): pass
class sub(op): pass
class mul(op): pass
class truediv(op): pass
class mod(op): pass
class pow(op): pass