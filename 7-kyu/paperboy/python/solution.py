def cheapest_quote(n):
	rates = [(40, 3.85), (20, 1.93), (10, 0.97), (5, 0.49), (1, 0.1)]
	total = 0
	papers = n
	for i in range(len(rates)):
		q, r = divmod(papers, rates[i][0])
		total += q * rates[i][1]
		papers = r
	return round(total, 2)
	
    