ALPHABET = ('a'..'z').zip((1..26)).to_h

def alpha_seq(s)
  s.downcase.chars.sort
    .map{|c| c.upcase + c * (ALPHABET[c] - 1)}
    .join(',')
end