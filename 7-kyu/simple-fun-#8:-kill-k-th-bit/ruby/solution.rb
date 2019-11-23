def kill_kth_bit(n, k)
  (n >> (k-1)) & 1 == 1 ? n - (1 << (k-1)) : n
end