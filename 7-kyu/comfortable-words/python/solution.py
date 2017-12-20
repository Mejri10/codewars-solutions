def comfortable_word(word):
  left, right = 'qwertasdfgzxcvb', 'yuiophjklnm'
  isconfortable = True
  for i in range(len(word) - 1):
      if word[i] in left and word[i+1] in left or word[i] in right and word[i+1] in right:
          isconfortable = False
          break
  return isconfortable
  