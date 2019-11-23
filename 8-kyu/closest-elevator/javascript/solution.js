function elevator(left, right, call){
  const dLeft = Math.abs(call - left);
  const dRight = Math.abs(call - right);
  return dLeft < dRight ? "left" : "right";
}