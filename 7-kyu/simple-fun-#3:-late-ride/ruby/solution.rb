def late_ride(n)
  (Time.new(0) + (n * 60)).strftime("%k%M").to_i.digits.sum
end