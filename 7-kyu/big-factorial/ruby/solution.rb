def factorial(n)
  return nil if n < 0

  result = 1
  while n > 1
    result *= n
    n -= 1
  end
  result
end