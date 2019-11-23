function productArray(numbers){
  const totalProd = numbers.reduce((total, n) => total * n, 1);
  return numbers.map(n => totalProd/n);
}