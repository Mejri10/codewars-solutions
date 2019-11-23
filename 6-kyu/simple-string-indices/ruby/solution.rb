def solve(s, n)
  return -1 if s[n] != '('
  sum = 0
  s[n..-1].chars.each_with_index do |c, idx|
    value = case c
      when '(' then  1
      when ')' then -1
      else 0
    end  
    sum += value
    return idx + n if sum == 0
  end
  return -1
end