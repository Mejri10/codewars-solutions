function ipv4Value(ipv4Address) {
  return ipv4Address
           .split('.')
           .map((octet, idx) => parseInt(octet) * Math.pow(256, 3 - idx))
           .reduce((acc, n) => acc + n)
}

function ipsBetween(start, end){
  return ipv4Value(end) - ipv4Value(start);
}