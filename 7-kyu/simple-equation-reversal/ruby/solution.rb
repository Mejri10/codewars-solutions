def solve(eq)
  eq.gsub(/(\d+)/){ |n| n.reverse }
    .reverse
end