function solve(a,b){
  return b.match('^' + a.replace('*', '[a-z]*') + '$') !== null;
}