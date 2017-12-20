def split_exp(n):
  if '.' in n:
      whole, decimal = n.split('.')
      return split_exp(whole) + ['.' + '0'*len(n[:i]) + d for i, d in enumerate(decimal) if d != '0']
  else:
      return [d + '0'*len(n[i+1:]) for i, d in enumerate(n) if d != '0']