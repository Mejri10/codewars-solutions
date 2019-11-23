def sum_of_threes(n)
  n_base3 = n.to_s(3)
  if n_base3.include?("2")
    "Impossible"
  else
    size = n_base3.length
    n_base3.chars.each_with_index.reduce([]) do |builder, (d, idx)|
      builder << "3^#{size - idx - 1}" if d != '0'
      builder
    end.join('+')
  end
end