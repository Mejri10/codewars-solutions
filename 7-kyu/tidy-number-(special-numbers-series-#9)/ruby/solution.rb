def tidy_number(n)
  (digits = n.to_s.chars).sort == digits
end