function distribute(candies, children) {
  if (children <= 0) {
    return [];
  }

  candies = Math.max(candies, 0);
  let quotient = Math.floor(candies / children)
  let remainder = candies % children
  
  return [...new Array(children)].map(n =>
    quotient + (remainder-- > 0 ? 1 : 0)
  )
}