Array.prototype.sum = function() {
  return this.reduce((partialSum, n) => partialSum + n, 0);
}

Array.prototype.mean = function () {
  if (this.length === 0) {
    return 0;
  }
  return this.sum()/this.length;
}

Array.prototype.std = function() {
  if (this.length === 0) {
    return 0;
  }
  const mean = this.mean();
  const diffFromMean = this.reduce((partialSum, n) => 
  partialSum + Math.pow(n - mean, 2) , 0);
  
  return Math.pow(diffFromMean/this.length, 0.5);
}

function stdFilter(arr) {
  const mean = arr.mean();
  const std = arr.std();
  const arrFiltered = arr.filter(n => 
    n >= (mean - 2.5*std) && n <= (mean + 2.5*std)
  )
  if (arrFiltered.length === arr.length) {
    return arrFiltered;
  } else {
    return stdFilter(arrFiltered);
  }
}

function filterVal(lst){
  const lstFiltered = stdFilter(lst);
  return [
    [lst.length, lstFiltered.length],
    lstFiltered.mean(),
    lstFiltered.std()/Math.pow(lstFiltered.length, 0.5)
  ];
}