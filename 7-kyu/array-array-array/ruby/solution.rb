def explode arr
  [arr] * arr.select{|e| e.class == Fixnum }.reduce(&:+) rescue "Void!"
end