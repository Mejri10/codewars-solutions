from string import maketrans

rules ={
  'A' : '@',
  'B' : '8',
  'C' : '(',
  'D' : 'D',
  'E' : '3',
  'F' : 'F',
  'G' : '6',
  'H' : '#',
  'I' : '!',
  'J' : 'J',
  'K' : 'K',
  'L' : '1',
  'M' : 'M',
  'N' : 'N',
  'O' : '0',
  'P' : 'P',
  'Q' : 'Q',
  'R' : 'R',
  'S' : '$',
  'T' : '7',
  'U' : 'U',
  'V' : 'V',
  'W' : 'W',
  'X' : 'X',
  'Y' : 'Y',
  'Z' : '2',
}

def to_leet_speak(s):
    translationRule = maketrans(''.join(rules.keys()), ''.join(rules.values()))
    return s.translate(translationRule)
