def positive_sum(arr)
  arr.sum{|x| x > 0 ? x : 0}
end
