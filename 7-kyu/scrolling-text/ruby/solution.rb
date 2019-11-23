def scrolling_text(text)
  (0...text.length).each_with_index.map{ |c, idx| (text * 2).upcase[idx...(idx + text.length)] }
end