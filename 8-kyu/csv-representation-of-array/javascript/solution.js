function toCsvText(array) {
   return array
   .map(line => line.join(","))
   .join("\n");
}