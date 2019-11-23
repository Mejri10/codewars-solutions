const mainDiagonal = matrix =>
  matrix.map((row, i) => row[i]);

const secondaryDiagonal = matrix =>
  matrix.map((row, i) => row[row.length - 1 - i]);

const sumArray = array =>
  array.reduce((x, y) => x + y, 0);

function diagonal(matrix){
  const sumMainDiagonal = sumArray(mainDiagonal(matrix));
  const sumSecondaryDiagonal = sumArray(secondaryDiagonal(matrix));
  
  if (sumMainDiagonal > sumSecondaryDiagonal) {
    return "Principal Diagonal win!";
  } else if (sumMainDiagonal < sumSecondaryDiagonal) {
    return "Secondary Diagonal win!";
  } else {
    return "Draw!";
  }
}
