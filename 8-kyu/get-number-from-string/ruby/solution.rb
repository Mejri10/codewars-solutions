def get_number_from_string(s)
  s.scan(/\d+/).join.to_i
end