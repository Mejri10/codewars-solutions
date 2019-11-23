def even_numbers(arr,n)
  arr.select(&:even?).reverse[0...n].reverse
end