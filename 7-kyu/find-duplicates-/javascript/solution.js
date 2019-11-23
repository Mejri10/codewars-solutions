function duplicates(arr) {
  const ans = [];
  arr.forEach((n, idx) => {
    if (!ans.includes(n) && arr.slice(idx+1).indexOf(n) !== -1) {
      ans.push(n);
    }
  });
  return ans;
}