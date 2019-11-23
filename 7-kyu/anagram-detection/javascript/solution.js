function charFrequency(string) {
  let frequency = new Map();
  string.toLowerCase().split('').forEach(char => {
    frequency.set(char, (frequency.get(char) || 0) + 1);
  })
  return frequency;
}

function compareMaps(map1, map2) {
  if (map1.size !== map2.size) return false ;
  
  let equals = true
  for (key of map1.keys()) {
    if (map1.get(key) !== map2.get(key)) {
      equals = false;
      break
    }
  }
  return equals;
}


function isAnagram(test, original) {
  return compareMaps(charFrequency(test), charFrequency(original));
};
