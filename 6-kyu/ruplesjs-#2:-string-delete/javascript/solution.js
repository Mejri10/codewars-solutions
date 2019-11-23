String.prototype.delete = function(...args) {
  return args.reduce((string, arg) => {
    if (typeof arg === 'string') {
      return string.replace(new RegExp(arg, "g"), "");
    } else if (arg instanceof RegExp) {
      return string.replace(arg, "");
    } else {
      return string;
    }
  }, this.toString())
}