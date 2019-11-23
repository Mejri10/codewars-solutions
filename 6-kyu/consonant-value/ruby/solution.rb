def string_value str
  str.chars.map{ |c| c.ord - 96 }.reduce &:+
end

def solve str
  consonants = str.scan /[^aeiou]+/
  consonants.map{ |c| string_value(c) }.max
end