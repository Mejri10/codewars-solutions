import re

def get_issuer(number):
  number = str(number)
  if re.match(r"^(34|37)\d{13}$",number):
      return "AMEX"
  elif re.match(r"^6011\d{12}$",number):
      return "Discover"
  elif re.match(r"^(51|52|53|54|55)\d{14}$",number):
      return "Mastercard"
  elif re.match(r"^4(\d{12}|\d{15})$",number):
      return "VISA"
  else:
      return "Unknown"