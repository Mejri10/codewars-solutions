def weather_info(t):
    c = convertToCelsius(t)
    if (c < 0):
        return ("{} is freezing temperature".format(c))
    else:
        return ("{} is above freezing temperature".format(c))
    
def convertToCelsius(t):
  return (t - 32) * (float(5)/9)
