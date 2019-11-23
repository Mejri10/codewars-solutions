function bouncingBall(initial, proportion) {
  let count = 0;
  while(initial > 1) {
    initial *= proportion;
    count++;
  }
  return count;
};