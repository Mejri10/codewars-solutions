def solve(s)
  mismatches = 0
  s.chars.zip(s.reverse.chars).each { |a, b| mismatches += 1 if a != b }
  (mismatches == 2 || (mismatches == 0 && s.length.odd?)) ? true : false
end