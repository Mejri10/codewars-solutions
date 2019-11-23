def int32_to_ip(int32)
  int32.to_s(2).rjust(32, "0").chars.each_slice(8).map{|n| n.join.to_i(2)}.join('.')
end