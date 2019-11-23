function bubblesortOnce(a) {
  const newArr = [...a];
  for (let i = 0; i < newArr.length - 1; i++) {
    if (newArr[i] > newArr[i+1]) {
      let temp = a[i+1];
      newArr[i+1] = newArr[i];
      newArr[i] = temp;
    }
  }
  return newArr;
}