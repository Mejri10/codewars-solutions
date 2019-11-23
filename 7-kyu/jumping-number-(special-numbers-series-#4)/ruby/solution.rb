def jumping_number(n)
  n.digits.each_cons(2).map{|a,b| (a-b).abs - 1}.all?(&:zero?) ?
    "Jumping!!":
    "Not!!"
end