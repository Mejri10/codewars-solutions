def repeats(arr)
  freq = Hash.new(0)
  arr.each{ |n| freq[n] += 1 }
  freq.select{ |k, v| v == 1 }.keys.reduce &:+
end