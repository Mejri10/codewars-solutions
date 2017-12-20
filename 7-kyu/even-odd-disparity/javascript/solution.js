function solve(a){
  const odds = a.filter(x => typeof(x) === 'number' && x % 2 !== 0);
  const evens = a.filter(x => typeof(x) === 'number' && x % 2 === 0);
  return evens.length - odds.length;
};