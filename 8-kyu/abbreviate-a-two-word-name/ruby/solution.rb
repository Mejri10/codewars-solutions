def abbrev_name(name)
  name.split.map{ |w| w[0].upcase }.join('.')
end