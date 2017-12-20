"""
WARNING: POORLY WRITTEN CODE BELOW
Maybe someday I will refactor this...
"""


class Arith():
    NUMS = {"zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "eleven": 11,
            "twelve": 12,
            "thirteen": 13,
            "fourteen": 14,
            "fifteen": 15,
            "sixteen": 16,
            "seventeen": 17,
            "eighteen": 18,
            "nineteen": 19,
            "twenty": 20,
            "thirty": 30,
            "forty": 40,
            "fifty": 50,
            "sixty": 60,
            "seventy": 70,
            "eighty": 80,
            "ninety": 90
    }
    STRINGS = {v: k for k, v in NUMS.items()}
    
    def __init__(self, numstring=""):
        self.numstring = numstring
    
    def toInt(self):
        seps = (("thousand", 1000), ("hundred", 100))
        total = 0
        string = self.numstring
        for sep, factor in seps:
            s = string.split(sep)
            if len(s) > 1:
                total += self.NUMS[s[0].strip()] * factor
                string = "".join(s[1:])
        string = string.replace("and", "").strip()
        for num in string.split():
            total += self.NUMS[num]
        return total
            
    def toString(self, num):
        seps = ((1000, "thousand"), (100, "hundred"))
        string = []
        for factor, sep in seps:
            whole, remainder = divmod(num, factor)
            if whole > 0:
                string.extend([self.STRINGS[whole], sep])
                num = remainder
        if num == 0:
            return " ".join(string).strip() 
        else:
            if string:
                string.append("and")
            if num >= 20:
                whole, remainder = divmod(num, 10)
                string.extend([self.STRINGS[whole*10], self.STRINGS[remainder] if remainder else ""])
            else:
                string.append(self.STRINGS[num])                
            return " ".join(string).strip()           
        
    
    def add(self, value):
        return Arith().toString(self.toInt() + Arith(value).toInt())