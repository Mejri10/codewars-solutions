def doubles(s)
  s_copy = s.dup
  loop do
    s_new = s_copy.gsub /(\w)\1/, ""
    break if s_new == s_copy
    s_copy = s_new
  end
  s_copy
end