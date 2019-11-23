require 'set'

def next_id(arr)
  (Set.new(0..((arr.max || 0) + 1)) - arr).min
end