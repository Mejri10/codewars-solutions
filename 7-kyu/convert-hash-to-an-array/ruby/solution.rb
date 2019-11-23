def convert_hash_to_array(hash)
  hash.reduce([]) { |prev, (k, v)| prev.push([k.to_s, v]); prev }
end