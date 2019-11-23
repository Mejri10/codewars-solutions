def in_array(array1, array2)
  array1.select{ |w1| array2.any?{ |w2| w2.include?(w1) } }.sort
end
