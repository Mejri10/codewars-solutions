def oddball x
  odd_index = x.index('odd')
  x.any? { |n| n.class == Integer && n == odd_index }
end