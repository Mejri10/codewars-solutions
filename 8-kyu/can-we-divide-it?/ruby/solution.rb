def is_divide_by(number, *args)
  args.all?{|n| number % n == 0}
end