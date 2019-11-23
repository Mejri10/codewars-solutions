def men_from_boys(arr)
  even = arr.select(&:even?).uniq.sort
  odd = arr.select(&:odd?).uniq.sort.reverse
  even + odd
end