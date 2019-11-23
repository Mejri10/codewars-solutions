def high(x)
  words = x.split
  word_values = words.map(&:chars).map { |arr| arr.map { |c| c.ord - 96 }.reduce(&:+) }
  max_idx = word_values.index(word_values.max)
  words[max_idx]
end