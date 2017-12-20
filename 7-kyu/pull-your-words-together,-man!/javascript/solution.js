function sentencify(words) {
  const sentence = words.join(' ');
  return sentence[0].toUpperCase() + sentence.slice(1) + '.';
}
