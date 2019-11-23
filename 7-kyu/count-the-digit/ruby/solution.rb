def nb_dig(n, d)
	(0..n).map{ |i| i * i }.map(&:to_s).join.count(d.to_s)
end