def persistence(n)
  count = 0
  begin
    count = n > 9 ? count + 1 : count
  end while (n = n.digits.reduce(&:*)) > 9
  count
end