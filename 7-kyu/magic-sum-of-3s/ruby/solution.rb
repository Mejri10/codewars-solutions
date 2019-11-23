def magic_sum(numbers)
	numbers.nil? ? 0 : numbers.select{ |n| n.odd? && n.to_s.include?("3") }.reduce(0, &:+)
end