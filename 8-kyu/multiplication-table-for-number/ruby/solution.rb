def multiTable(number)
  (1..10).map{ |n| "#{n} * #{number} = #{n * number}" }.join("\n")
end