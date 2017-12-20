class Arith():
    
    numerals = ["zero",
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
                "ten",
                "eleven",
                "twelve",
                "thirteen",
                "fourteen",
                "fifteen",
                "sixteen",
                "seventeen",
                "eighteen",
                "nineteen",
                "twenty"
                ]
                
    numbers = list(range(0, 21))
    
    num2numeral = dict(zip(numbers, numerals))
    numeral2num = dict(zip(numerals, numbers))
    
    def __init__(self, value):
        self.value = value
    def add(self, n):
        return self.num2numeral[self.numeral2num[self.value] + self.numeral2num[n]]
        