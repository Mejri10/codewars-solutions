def count_position
  Proc.new { |s| s.chars.select.with_index { |c, i| c.downcase.ord - 97 == i }.count }
end

def solve(arr)
  arr.map &count_position
end