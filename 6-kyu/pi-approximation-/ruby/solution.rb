def iter_pi(epsilon)
  i, f = 0, 0
  while (Math::PI - f).abs > epsilon
    i += 1
    f += 4 * (-1)**(i+1) / (2.0*i - 1)
  end
  [i, f.round(10)]
end