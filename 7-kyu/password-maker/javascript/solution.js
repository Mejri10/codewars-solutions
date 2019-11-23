const secretMapping = {
  i: "1",
  o: "0",
  s: "5"
}

function makePassword(phrase) {
  return phrase
          .split(' ')
          .map(word => secretMapping[word[0].toLowerCase()] || word[0])
          .join('')
          
}