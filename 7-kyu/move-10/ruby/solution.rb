def move_ten st
  st.chars.map{ |c| (97 + (c.ord - 87) % 26).chr }.join
end