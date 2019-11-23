const G = 6.67 * Math.pow(10, -11);
const CONVERSION_FACTORS = {
  "kg": 1,
  "g" : Math.pow(10, -3),
  "mg": Math.pow(10, -6),
  "μg": Math.pow(10, -9),
  "lb": 0.453592,
  "m" : 1,
  "cm": Math.pow(10, -2),
  "mm": Math.pow(10, -3),
  "μm": Math.pow(10, -6),
  "ft": 0.3048,
}

solution = (arr_val, arr_unit) => {
  const [m1, m2, d] = arr_val.map((val, i) => val * CONVERSION_FACTORS[arr_unit[i]]);
  
  return G*m1*m2/Math.pow(d, 2); 
};