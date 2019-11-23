def ordered_count(str)
  str.chars
  .reduce({}){|freq, c| freq[c] = (freq[c] || 0) + 1; freq}
  .to_a
end