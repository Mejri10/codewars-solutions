def solve(arr)
  ans = []
  arr_sorted = arr.sort
  until arr_sorted.empty?
    ans.push arr_sorted.pop
    ans.push arr_sorted.shift
  end
  ans.compact
end