def is_vow(a)
  a.map { |d| "aeiou".include?(d.chr)? d.chr : d }
end