def sort_the_inner_content(words):
  return ' '.join([word[0] + ''.join(sorted(word[1:-1], reverse=True)) + word[-1] if len(word) > 1 else word for word in words.split()])
