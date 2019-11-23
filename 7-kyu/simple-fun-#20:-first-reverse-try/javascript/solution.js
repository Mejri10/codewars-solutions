function firstReverseTry(arr) {
  if (arr.length < 2) {
    return arr;
  }

  const first = arr[0];
  const middle = arr.slice(1, -1);
  const last = arr[arr.length - 1];
  return [last].concat(middle).concat([first]);
  
}