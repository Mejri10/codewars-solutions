function Node(data) {
  this.data = data;
  this.next = null;
}

function append(listA, listB) {
  if (listA === null && listB === null) return null;
  if (listA == null) return listB;
  if (listB == null) return listA;
  
  let node = listA;
  while (node.next !== null) { node = node.next }
  node.next = listB;
  return listA;
}  