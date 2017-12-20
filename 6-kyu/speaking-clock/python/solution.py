num2str = {
    0: "midnight",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "noon",
    15: "quarter",
    20: "twenty",
    25: "twenty-five",
    30: "half"
}

class WorldClock(object):

    @classmethod
    def get_time_text(cls, h, m):
        m = ((m // 5) + (m % 5 != 0)) * 5
        if m == 60:
            m = 0
            h += 1            
        h = h % 12 if h != 0 and h != 12 else h        
        if m:
            if m <= 30:
                return "{} past {}".format(num2str[m], num2str[h])
            else:
                m = 60 - m
                h = (h + 1) % 12
                return "{} to {}".format(num2str[m], num2str[h])
        else:
            return "{}".format(num2str[h])
        