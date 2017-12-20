function zigZagCamel(d, h) {
  const pi = Math.PI;
  const alpha = Math.atan(h/d);
  if (alpha <= pi/6)
    return Math.hypot(d, h);
  else {
    let total = 0;
    while (h > 1e-12) {
  		let d1 = d;
  		let h1 = Math.tan(pi/6) * d1;
  		let h2 = (d1 - h1 * Math.tan(pi/2 - alpha))/(Math.tan(pi/3) + Math.tan(pi/2 - alpha));
  		let d2 = Math.tan(pi/3) * h2;
  		total += Math.hypot(d1, h1) + Math.hypot(d2, h2);
  		d = d2;
      h = h - (h1 + h2);
    }
    return total;
  }
}
