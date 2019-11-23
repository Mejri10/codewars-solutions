def split_and_add(arr, n)
  return arr if arr.size == 0 || n == 0
    
  firstHalf, secondHalf = arr[0...(arr.size/2)], arr[(arr.size/2)...(arr.size)]
  firstHalf.unshift(0) if arr.size.odd?
  
  split_and_add(firstHalf.zip(secondHalf).map{|a, b| a + b}, n - 1)
end