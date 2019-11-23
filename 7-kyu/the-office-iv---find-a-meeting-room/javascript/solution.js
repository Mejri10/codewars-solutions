function meeting(x){
  const index = x.indexOf('O');
  return  index == -1 ? 'None available!' : index;
}