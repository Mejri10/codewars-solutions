def small_enough(a, limit)
  a.all? {|n| n <= limit}
end