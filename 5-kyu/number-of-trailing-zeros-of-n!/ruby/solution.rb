def zeros(n)
  i, count = 5, 0
  while n/i > 0
    count += n/i
    i *= 5
  end 
  count;
end