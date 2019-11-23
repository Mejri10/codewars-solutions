function createPhoneNumber(numbers){
  const areaCode = numbers.slice(0, 3).join("");
  const preffix = numbers.slice(3, 6).join("");
  const suffix = numbers.slice(6, numbers.length).join("");
  return `(${areaCode}) ${preffix}-${suffix}`;
}