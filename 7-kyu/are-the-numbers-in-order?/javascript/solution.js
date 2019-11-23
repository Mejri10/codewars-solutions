function inAscOrder(arr) {
  let ordered = true;
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      ordered = false;
      break;
    }
  }
  return ordered;
}