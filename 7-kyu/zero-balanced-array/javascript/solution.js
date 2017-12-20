function ìsZeroBalanced(n){
  if (n.length < 1)
    return false;
  else
    return n.reduce((x, y) => x + y) === 0 && 
    (n.sort().toString() === n.map(x => -x).sort().toString());
}