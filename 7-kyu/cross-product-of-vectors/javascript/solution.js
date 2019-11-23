function is3DVector(vector) {
  return Array.isArray(vector) && vector.length === 3;
}

function crossProduct (vector1, vector2) {
  if (!is3DVector(vector1) || !is3DVector(vector2)) {
     throw "Arguments are not 3D vectors!";
  }
  
  const [x1, y1, z1] = vector1;
  const [x2, y2, z2] = vector2;
  
  return [
    y1*z2 - z1*y2,
    z1*x2 - x1*z2,
    x1*y2 - x2*y1
  ]
}