def delete_digit(n)
  digits = n.to_s.chars
  (0...digits.length).reduce([]) do |arr, idx|
    arr << (digits[0...idx] + digits[(idx + 1)...(digits.length)]).join.to_i
    arr
  end.max
end