def sum (arr)
  arr.reduce &:+
end


def peak(arr)
  arr.each_with_index do |n, idx|
    return idx if sum(arr[0...idx]) == sum(arr[idx+1..-1])
  end
  return -1
end