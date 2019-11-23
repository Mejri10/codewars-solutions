function adjacentElementsProduct(array) {
  return Math.max(...array
  .reduce((arr, _, idx) => {
    if (array[idx + 1] !== undefined) {
      arr.push(array[idx] * array[idx + 1]);
    }
    return arr;
  }, []))
}