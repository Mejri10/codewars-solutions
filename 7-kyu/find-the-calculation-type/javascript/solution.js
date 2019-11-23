const calcType = (a, b, res) => ({
  [a*b]: "multiplication",
  [a/b]: "division",
  [a+b]: "addition",
  [a-b]: "subtraction"
}[res])