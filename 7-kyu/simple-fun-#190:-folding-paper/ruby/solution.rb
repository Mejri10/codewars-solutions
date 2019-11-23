def folding(a,b)
  a, b = [a, b].sort
  a == b ? 1 : 1 + folding(a, b - a)
end