require 'set'

def is_all_possibilities(arr)
  return false if arr == []
  Set.new((0...arr.length)) == Set.new(arr)
end