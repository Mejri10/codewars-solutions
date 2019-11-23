def solution(keys, default_value)
  keys.map{|k| [k, default_value]}.to_h
end