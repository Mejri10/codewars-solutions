class SquareMatrix {

  constructor(arr) {
    if (!this.checkIfSquare(arr)) throw new Error("Matrix must be square to have a size.");

    this.matrix = arr;
    this.dim = arr.length
  }

  checkIfSquare(arr) {
    const nRows = arr.length;
    return arr.every(row => row.length === nRows);
  }

  getElem(i, j) {
    return this.matrix[i][j];
  }

  size() {
    return [this.dim, this.dim];
  }

  det() {
    return this.detHelper(this);
  }

  detHelper(matrix) {
    if (matrix.dim === 1) {
      return matrix.getElem(0, 0);
    } else {
      return matrix
              .matrix
              .map((row, idx) => row[0] * Math.pow(-1, idx) * this.cofactor(idx, 0).det())
              .reduce((prev, curr) => prev + curr, 0)
    }
  }

  cofactor(i, j) {
    let cofactor = [];
    this.matrix.forEach((row, rowIndex) => {
      if (!(i === rowIndex)) {
        let cofactorRow = [];
        row.forEach((colValue, colIndex) => {
          if (!(j === colIndex)) {
            cofactorRow.push(colValue);
          }
        })
        cofactor.push(cofactorRow)
      }
    })
    return new SquareMatrix(cofactor);
  }

  substituteColumn(arr, position) {
    if (arr.length !== this.dim) throw new Error(`Array must be of size ${this.dim}`);
    if (position > (this.dim - 1)) throw new Error(`position shoud be between 0 and ${this.dim - 1}`);

    let newMatrix = [];
    this.matrix.forEach((row, rowIndex) => {
      let newRow = [];
      row.forEach((col, colIndex) => {
        if (position === colIndex) newRow.push(arr[rowIndex]);
        else newRow.push(col);
      })
      newMatrix.push(newRow);
    })
    return new SquareMatrix(newMatrix);
  }
}

function cramerSolver(matrix, vector) { 
    let m;
    try {
      m = new SquareMatrix(matrix)
    } catch(e) {
      return 'Check entries';
    }

    if (m.dim !== vector.length) return 'Check entries';

    const det = m.det();
    const dets = [];

    for (let i = 0; i < vector.length; i++) {
      dets.push(m.substituteColumn(vector, i).det());
    }


    if (det === 0) {
      if (dets.every(det_i => det_i === 0)) {
        return "Indeterminate or Unsolvable";
      } else {
        return "Unsolvable";
      }
    } else {
      return [det, ...dets];
    }
}