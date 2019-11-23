def pipeline(*funcs)
  -> val { funcs.reduce(val) { |v, func| func.call(v) } }
end

def predict_age(*ages)
  square_array = -> arr { arr.map{ |n| n * n } }
  sum_array = -> arr { arr.reduce(0) { |sum, n| sum + n } }
  sqrt = -> n { Math.sqrt(n) }
  divide_by_2 = -> n { n/2 }
  floor = -> n { n.floor }
  
  pipeline(
    square_array,  
    sum_array,
    sqrt,
    divide_by_2,
    floor
  ).call(ages)
end