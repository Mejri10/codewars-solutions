function sumTimesTables(tables, min, max){
  if (tables.length < 1) return 0;
  return tables.reduce((x, y) => x + y) * (max + min)*(max - min + 1)/2;
}