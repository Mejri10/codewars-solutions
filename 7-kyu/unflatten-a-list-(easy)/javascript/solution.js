function unflatten (flatArray) {
  let ans = [];
  let i = 0;
  while (i < flatArray.length) {
    const currentValue = flatArray[i];
    if (currentValue < 3) {
      ans.push(currentValue);
      i++;
    } else {
      let subArray = [];
      for (let j = i; j < i + currentValue; j++) {
        if(flatArray[j] !== undefined) {
          subArray.push(flatArray[j]);
        }
      }
      ans.push(subArray);
      i += currentValue;
    }
  }
  return ans;
}