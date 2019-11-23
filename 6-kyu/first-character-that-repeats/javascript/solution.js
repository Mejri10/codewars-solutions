function letterFrequency(letters) {
  return letters.reduce((map, letter) =>
    map.set(letter, (map.get(letter) || 0) + 1),
    new Map()
  );
}

function duplicateLetters(letterFrequencies) {
  const letters = [];
  letterFrequencies.forEach((freq, letter) => {
    if (freq > 1) {
      letters.push(letter);
    }
  });
  return letters;
}

function firstDup(s) {
  const letters = s.split('');
  const frequencies = letterFrequency(letters);
  const duplicates = duplicateLetters(frequencies);
  return duplicates.sort((a, b) => letters.indexOf(a) > letters.indexOf(b))[0]
}