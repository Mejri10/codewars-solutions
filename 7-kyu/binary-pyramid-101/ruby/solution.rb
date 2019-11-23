def binary_piramid(m,n)
  (m..n).reduce(0){ |sum, i| sum + i.to_s(2).to_i }.to_s(2)
end