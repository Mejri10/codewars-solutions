def round_to_five(numbers)
  numbers.map { |n| (n/5.0).round * 5 }
end