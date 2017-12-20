function vertMirror(s) {
  let ans = [];
  s.split('\n').forEach(line =>
    ans.push(line.split('').reverse().join('')));
  return ans.join('\n');
}

function horMirror(s) {
  return s.split('\n').reverse().join('\n');
}

function oper(fct, s) {
   return fct(s);
}