def count_errors(s)
  s.chars.inject(Hash.new) do |hash, char|
    hash[char] = hash.fetch(char, 0) + 1 if %w(u w x z).include?(char)
    hash
  end
end

def format_error(letter, freq)
  "#{"%-2s" % letter} #{"%-6s" % freq}#{'*' * freq}"
end

def hist(s)
    count_errors(s)
      .sort
      .map{ |(letter, freq)| format_error(letter, freq) }
      .join("\r")
end