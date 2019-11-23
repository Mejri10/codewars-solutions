function isValidIP(str) {
  const octets = str.split('.');
  if (octets.length !== 4) return false;
  
  return octets.every(octet =>
    octet.match(/^(?!0)\d+$|^0$/) &&
    parseInt(octet) <= 255 &&
    parseInt(octet) >= 0
  );
}