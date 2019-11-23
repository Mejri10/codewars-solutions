Array.prototype.zip = function(other) {
  const size = Math.min(this.length, other.length);
  return this.slice(0, size).map((x, idx) => [x, other[idx]]);
}

function dot(a, b) {
  return a.zip(b).reduce((sum, [x, y]) => sum + x*y, 0);
}

function minDot(a,b){  
  return dot(
    a.slice().sort((x, y) => x - y),
    b.slice().sort((x, y) => y - x)
  )
}

