function convertHashToArray(hash){
  const arr = Object.entries(hash);
  arr.sort();
  return arr;
}