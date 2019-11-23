const countSheep = num => {
  let ans = "";
  for (let count = 1; count <= num; count++) {
    ans += `${count} sheep...`;
  }
  return ans;
}