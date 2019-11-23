def meeting(s)
  s.split(";")
    .map{|person| person.split(":").map(&:upcase).reverse}
    .map{|(first_name, last_name)| "(#{first_name}, #{last_name})"}
    .sort
    .join
end