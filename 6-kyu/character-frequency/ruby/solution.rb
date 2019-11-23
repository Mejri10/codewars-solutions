def letter_frequency(text)
  text.downcase
      .gsub(/[^a-z]/, '')
      .chars
      .inject(Hash.new(0)){ |hash, c| hash[c] += 1; hash }
      .sort
      .sort_by.with_index{ |(letter, freq), idx| [-freq, idx] }
end