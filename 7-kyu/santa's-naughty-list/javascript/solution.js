const findChildren = (santasList, children) =>
  [...new Set(children.filter(c => santasList.includes(c)))].sort();