const solve = s => Math.max(...s.match(/[aeiou]+/g).map(n => n.length));
