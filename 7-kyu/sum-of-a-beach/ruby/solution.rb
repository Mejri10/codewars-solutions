def sum_of_a_beach(beach)
  ["sand", "water", "fish", "sun"].reduce(0) { |sum, w| sum + beach.downcase.scan(w).length }
end