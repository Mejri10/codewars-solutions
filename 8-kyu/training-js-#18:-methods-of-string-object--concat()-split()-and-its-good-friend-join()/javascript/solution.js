const splitAndMerge = (str,sp) => 
  str.split(" ").map(w => w.split("").join(sp)).join(" ")