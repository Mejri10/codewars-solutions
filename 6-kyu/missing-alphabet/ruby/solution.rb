def insert_missing_letters(st)
    letters = st.split('')
    letters_uniq = letters.uniq
    missing_letters = (("a".."z").to_a - letters_uniq)
    ans = ""
    letters.each do |l|
      if letters_uniq.include? l
        ans << l + missing_letters.select{ |ml| ml > l }.map(&:upcase).join
        letters_uniq -= [l]
      else
         ans << l
      end
    end
    ans
end