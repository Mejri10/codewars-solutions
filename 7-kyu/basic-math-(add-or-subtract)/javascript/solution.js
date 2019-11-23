function calculate(str) {
  return eval(
    str.replace(new RegExp("plus", "g"), "+")
       .replace(new RegExp("minus", "g"), "-")
  ).toString()
}