const countAnimals = sentence =>
  (sentence.match(/\d+/g) || [])
    .map(num => parseInt(num, 10))
    .reduce((a, b) => a + b, 0)