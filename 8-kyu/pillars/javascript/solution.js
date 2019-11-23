function pillars(numPill, dist, width) {
  const totalDistance = numPill*width + dist*100*(numPill - 1);
  return Math.max(0, totalDistance - 2*width);
}