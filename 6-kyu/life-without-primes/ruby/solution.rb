def prime?(n)
  is_prime = (n <= 1) ? false : true
  (2..(n**0.5).floor).each do |i|
    if n % i == 0
      is_prime = false
      break
    end
  end
  is_prime
end

def has_prime_digit?(n)
  n.to_s.chars.any? { |i| prime?(i.to_i) }
end

def solve(n)
  nums = []; i = 1
  i = 1
  while nums.length < (n + 1)
    nums.push(i) if !prime?(i) && !has_prime_digit?(i)
    i += 1
  end
  nums.last
end