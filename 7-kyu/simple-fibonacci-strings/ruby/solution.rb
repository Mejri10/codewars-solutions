def solve(n)
  n < 2 ? ( n < 1 ? '0' : '01' ) : solve(n-1) + solve(n-2)
end