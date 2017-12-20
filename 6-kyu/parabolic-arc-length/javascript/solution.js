function lenCurve(n) {
  const h = 1/n;
  const y = x => x * x;
  let len = 0;
  for (let i = 0; i < n; i++) {
      let xi = i * h;
      let xf = (i + 1) * h;
      len += Math.sqrt(Math.pow(y(xf) - y(xi), 2) + Math.pow(xf - xi, 2), 2);
      len = Math.round(len * 1e9)/1e9;
  }
  return len
}