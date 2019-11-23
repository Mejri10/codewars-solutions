function invertHash(hash) {
  let invertedHash = {};
  for (key in hash) {
    if (hash.hasOwnProperty(key)) {
      invertedHash[hash[key]] = key;
    }
  }
  return invertedHash;
}