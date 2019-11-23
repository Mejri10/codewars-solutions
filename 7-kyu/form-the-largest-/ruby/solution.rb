def max_number(n)
  n.to_s.chars.sort.reverse.join('').to_i
end