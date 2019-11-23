def invert_hash(hash)
  hash.reduce({}) { |h, (k, v)| h[v] = k; h }
end