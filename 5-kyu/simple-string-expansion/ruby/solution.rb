def solve s  
  match = s.match /([a-z]*)(\d*)\((.+)\)/ 
  if match.nil?
    s
  else
    outer, n, inner = match.captures
    outer + solve(inner) * (n.empty? ? 1 : n.to_i)
  end
end