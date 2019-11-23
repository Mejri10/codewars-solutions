function isPrime(n) {
  if (n === 1) return false;
  
  let prime = true;
  for (let i = 2; i < n/2; i++) {
    if (n % i == 0) {
      prime = false;
      break;
    }
  }
  return prime;
}

function isOdd(n) {  
 return (n & 1) === 1;
}

function oddNotPrime(n){
  let count = 0;
  for (let i = 1; i <= n; i++) {
    if (isOdd(i) && !isPrime(i)) count++;
  }
  return count;
}