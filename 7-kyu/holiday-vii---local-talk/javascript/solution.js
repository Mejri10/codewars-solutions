function pak(s){
  if(s.match(/^\s*$/)) {
    return '';
  }
  
  return s.split(' ').join(' pak ');
}