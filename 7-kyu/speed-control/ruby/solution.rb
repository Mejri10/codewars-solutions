def gps(s, x)
  x.each_cons(2).map{ |(a, b)| 3600*(b-a)/s }.max || 0
end