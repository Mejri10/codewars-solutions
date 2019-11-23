def flat_map list, &block
  list.map(&block).flatten
end