function alphabetPosition(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z]/g, '')
    .split('')
    .map(c => c.charCodeAt(0) - 96 + '')
    .join(' ')
}