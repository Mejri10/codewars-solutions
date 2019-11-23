require 'set'

def digits n
  n.to_s.chars.map &:to_i
end

def compute_depth n 
 set = Set.new 0..9
 count = 0
 until set.empty?
   count += 1
   set -= digits(n * count)
 end
 count
end