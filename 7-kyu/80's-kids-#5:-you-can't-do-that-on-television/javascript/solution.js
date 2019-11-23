const WATER_REGEX = /wet|water[a-z]*|wash[a-z]*/i;
const SLIME_REGEX = /i don\'t know|slime/i;

function bucketOf(str) {
  console.log(str);
  if (WATER_REGEX.test(str) && SLIME_REGEX.test(str)) {
    return "sludge";
  }
  
  if (WATER_REGEX.test(str)) {
    return "water";
  }
  
  if (SLIME_REGEX.test(str)) {
    return "slime";
  }
  
  return "air";
}