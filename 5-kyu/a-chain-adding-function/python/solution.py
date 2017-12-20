"""
Copied from https://stackoverflow.com/questions/39038358/function-chaining-in-python
Author: Jim Fasarakis Hilliard
"""

class CustomInt(int):
    def __call__(self, v):
        return CustomInt(self + v)

def add(n):
    return CustomInt(n)