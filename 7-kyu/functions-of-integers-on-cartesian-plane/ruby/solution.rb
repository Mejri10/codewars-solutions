def sumin(n)
  n.downto(1).zip((1...(2*n)).step(2)).sum{|(a, b)| a * b}
end

def sumax(n)
  (1..n).zip((1...(2*n)).step(2)).sum{|(a, b)| a * b}
end

def sumsum(n)
  (2..(n+1)).sum{|i|(2.0*i + n-1) * n/2.0}
end