const isPrime = (n) => {
  if (n <= 2) return false;

  let prime = true;
  for (let i = 2; i < Math.floor(n/2); i++){
      if (n % i == 0){
          prime = false;
          break;
      }
  }
  return prime;
}

const isTwinPrime = n => 
isPrime(n) && (isPrime(n - 2) || isPrime(n + 2));