def near_flatten(arrays)
  near_flatten_unordered(arrays).sort
end

def near_flatten_unordered(arrays)
  ans = []
  arrays.map do |array| 
    if has_nested_array?(array)
      near_flatten_unordered(array).each { |arr| ans << arr }
    else 
      ans << array
    end
  end
  ans
end

def has_nested_array?(array)
  array.any? { |elem| elem.class == Array }
end