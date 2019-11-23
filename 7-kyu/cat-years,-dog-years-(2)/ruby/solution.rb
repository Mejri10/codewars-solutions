def convertion(years, first_year, second_year, after_years)
  if years < first_year
    0
  elsif years < first_year + second_year
    1
  elsif years == first_year + second_year
    2
  else
    2 + (years - first_year - second_year) / after_years
  end
end

def owned_cat_and_dog(cat_years, dog_years)
  return [convertion(cat_years, 15, 9, 4), convertion(dog_years, 15, 9, 5)]
end