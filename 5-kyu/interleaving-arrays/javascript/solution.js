function interleave(...arr) {
  if (!arr.every(Array.isArray)) {
    return [];
  }
  
  const longestArrayLength = Math.max(...arr.map(a => a.length))
  const result = [];
  for (let i = 0; i < longestArrayLength; i++) {
    for (let j = 0; j < arr.length; j++) {
      result.push(arr[j][i] || null);
    }
  }
  return result;
}