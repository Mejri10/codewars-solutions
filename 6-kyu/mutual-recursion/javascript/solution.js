function F(n) { 
  return n < 1? 1: n - M(F(n - 1));
}

function M(n) { 
  return n < 1? 0: n - F(M(n - 1));
}