def check_exam(arr1,arr2)
  [arr1.zip(arr2).map{|a, b| a == b ? 4 : b == '' ? 0 : -1 }.sum, 0].max
end