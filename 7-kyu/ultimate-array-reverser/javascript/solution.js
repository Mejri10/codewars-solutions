const ultimateReverse = s => {
  const result = [];
  const arrayReversed = s.join("").split("").reverse();
  let idx = 0;
  for (let i = 0; i < s.length; i++) {
    result.push(
      arrayReversed.slice(
        idx,
        idx + s[i].length
      ).join("")
    );
    idx += s[i].length
  }
  return result;
}