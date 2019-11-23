def is_prime?(n)
  prime = true
  sqrt_n_floored = (n**0.5).to_i
  for i in (2..sqrt_n_floored)
    if n % i == 0
      prime = false
      break
    end
  end
  prime
end

def digits_are_prime?(n)
  n.digits.all? { |d| [2,3,5,7].include?(d) }
end


def not_primes(a,b)
  (a...b).select { |n| digits_are_prime?(n) && !is_prime?(n) }
end