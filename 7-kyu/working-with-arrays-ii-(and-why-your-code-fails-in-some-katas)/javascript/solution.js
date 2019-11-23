const removeNthElement = (arr, n) =>
  [...arr.slice(0, n), ...arr.slice(n+1)];