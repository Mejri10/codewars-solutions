const squareArray = arr => arr.map(v => v * v);
const sumArray = arr => arr.reduce((sum, v) => sum + v);
const divideByTwo = n => n / 2;

const pipeline = (...funcs) => val => funcs.reduce((v, func) => func(v), val);

const predictAge = (...ages) => 
   pipeline(
    squareArray,
    sumArray,
    Math.sqrt,
    divideByTwo,
    Math.floor
  )(ages);