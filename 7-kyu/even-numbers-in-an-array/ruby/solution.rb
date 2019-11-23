def even_numbers(arr,n)
  arr.select(&:even?).reverse.take(n).reverse
end