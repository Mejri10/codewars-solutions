def prime_factors(n)
  ans = []
  i = 2
  while n > 1
    if n % i == 0
      ans << i
      n /= i
    else
      i += 1
    end
  end
  ans
end