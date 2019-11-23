function findDup( arr ){
  const arrSum = arr.reduce((acc,n) => acc + n, 0);
  const rangeSum = (1 + arr.length)*arr.length/2 - arr.length;
  return arrSum - rangeSum;
}