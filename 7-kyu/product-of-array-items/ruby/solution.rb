def product(arr)
  return nil if arr.nil? || arr.empty?
  arr.compact.reduce(1) { |prod, n| prod * n }
end
