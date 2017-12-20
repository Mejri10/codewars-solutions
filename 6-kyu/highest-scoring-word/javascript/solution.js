function high(x){
  const values = x.split(' ').map(word => {
    let total = 0;
    for (let i = 0; i < word.length; i++)
      total += word[i].charCodeAt() - 96;
    return total;
    });
  return x.split(' ')[values.indexOf(Math.max(...values))];  
}