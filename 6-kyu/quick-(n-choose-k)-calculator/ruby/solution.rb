$memoization = {}

def factorial(n)
  unless $memoization.has_key?(n)
    $memoization[n] = n > 1 ? n * factorial(n - 1) : 1
  end
  $memoization[n]  
end


def choose(n,k)
  factorial(n)/(factorial(n - k) * factorial(k))
end