def solve st,a,b
 st[0...a] + st[a..b].reverse + (st[(b + 1)..-1] || '')
end