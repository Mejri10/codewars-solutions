class String
  def first_letter_upcase
    return true if self.match(/^[A-Z]/) else false
  end
  
  def first_letter_downcase
    return true if self.match(/^[a-z]/) else false
  end
end

def capitals_first(string)
  words = string.split(" ")
  upcase = words.select(&:first_letter_upcase)
  downcase = words.select(&:first_letter_downcase)
  return (upcase + downcase).join(" ")
end