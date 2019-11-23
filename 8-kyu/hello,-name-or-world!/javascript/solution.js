String.prototype.capitalize = function() {
  return this
          .split(' ')
          .map(string => { 
            string = string.toLowerCase();
            return string.charAt(0).toUpperCase() + string.slice(1)
          });
}

function hello(name) {
  return `Hello, ${(name || 'world').capitalize()}!`;
}