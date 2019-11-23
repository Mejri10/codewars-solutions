@countcalls
def replicate(times, number):
  return [] if times <= 0 else [number] + replicate(times-1, number) 