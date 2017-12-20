function factorial(n) {
  return n === 1? 1 : n * factorial(n - 1);
}

function reverseFactorial(num) {
  let i = 1;
  while (factorial(i) < num) {
    i++;
  }
  if (factorial(i) > num)
    return 'None';
  else
    return `${i}!`;
}