KEYBOARD = [
 ['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
 ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
 ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
 ['p', 'q', 'r', 's', 't', '.', '@', '0'],
 ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']
]

def search_index(value)
  index = nil
  KEYBOARD.each_with_index do |row, i|
    j = row.index(value)
    index = [i, j] if j
  end
  index
end

def click_between_buttons(b1, b2)
  idx_b1, idx_b2 = search_index(b1), search_index(b2)
  idx_b1.zip(idx_b2).reduce(0){ |sum, elems| sum + elems.reduce(&:-).abs } + 1
end

def tv_remote(word)
  total = 0
  ("a" + word).chars.each_cons(2){ |chars| total += click_between_buttons(*chars) }
  total
end