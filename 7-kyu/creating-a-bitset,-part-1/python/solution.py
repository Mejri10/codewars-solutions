def byte_to_set(byte):
  bits = "{:08}".format(int(bin(byte)[2:]))
  return {n for n, b in zip(range(8), bits) if b == "1"}