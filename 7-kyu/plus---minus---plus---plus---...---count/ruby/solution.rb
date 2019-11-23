def catch_sign_change(arr)
  arr.each_cons(2).count{|a,b| a < 0 && b >= 0 || a >= 0 && b < 0}
end