"use strict";

Array.prototype.flatten = function() {
  const flattenedArray = [];
  this.map(value => {
    if(Array.isArray(value)) {
      if (value.length) flattenedArray.push(...value.flatten());
    } else {
      flattenedArray.push(value);
    }
  })
  return flattenedArray;
}

function flattenAndSort(array) {
  return array
          .flatten()
          .sort((a, b) => a > b ? 1 : a === b ? 0 : -1);
}