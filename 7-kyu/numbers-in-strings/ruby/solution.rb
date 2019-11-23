def solve(s)
  s.scan(/\d+/).map(&:to_i).max
end