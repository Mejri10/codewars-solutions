def dup(arr)
  arr.map { |word| word.gsub /([a-z])\1+/, '\1' }
end