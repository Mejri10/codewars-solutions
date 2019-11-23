function isNegativeZero(n) {
  return Number.isSafeInteger(n) && 1/n === Number.NEGATIVE_INFINITY;
}