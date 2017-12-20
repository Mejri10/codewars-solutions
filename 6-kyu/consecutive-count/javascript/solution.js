function getConsectiveItems(items, key){
  regex = new RegExp(key + '+', 'g');
  match = String(items).match(regex);
  if (match)
    return Math.max(...match.map(n => n.length));
  else
    return 0;
}