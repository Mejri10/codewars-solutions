def actually_really_good( foods )
	template = "You know what's actually really good? "
  if foods.length == 0
    template + "Nothing!"
  else
    good_foods = foods.uniq.sample(2)
    template + "#{good_foods.first.capitalize} and#{' more' if good_foods.length == 1} #{good_foods.last.downcase}."     
  end
end