function count (string) {  
  return string.split('').reduce((freq, c) => {
    freq[c] = (freq[c] || 0) + 1;
    return freq;
  }, {})
}