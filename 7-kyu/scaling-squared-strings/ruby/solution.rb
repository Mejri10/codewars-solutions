def scale(strng, k, n)
  strng.split("\n").reduce([]){|arr,s| arr + [s]*n}.map{|s| s.chars.map{|c| c*k}.join}.join("\n")
end