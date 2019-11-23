def matrixfy(x)
  return 'name must be at least one letter' if x.empty?
  size = (x.size**0.5).ceil
  ans = []
  x.chars.each_slice(size) { |slice| ans << slice + ['.'] * (size - slice.size) }
  ans << ['.'] * size unless ans.size == size
  ans
end  