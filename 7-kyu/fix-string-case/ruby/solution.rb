def solve s
  (s.size / 2) >= s.chars.select{ |c| c < 'a' }.size ? s.downcase : s.upcase
end