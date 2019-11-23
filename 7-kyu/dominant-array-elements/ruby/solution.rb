def solve(arr)  
 ans = []
 arr.each_with_index do |val, idx| 
   ans.push(val) if idx == (arr.size - 1) || arr[(idx + 1)..-1].max < val
 end
 ans
end