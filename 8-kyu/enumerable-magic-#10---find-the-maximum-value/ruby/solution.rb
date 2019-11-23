def max list, &block
  list.max{|a, b| block.call(a, b)}
end