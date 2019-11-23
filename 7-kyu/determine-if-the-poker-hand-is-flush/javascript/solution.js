function isFlush(cards) {
  const suits =  cards.map(card => card[card.length - 1])
  let flush = true;
  for (let i = 0; i < suits.length - 1; i++) {
    if (suits[i] !== suits[i + 1]) {
      flush = false;
      break;
    }
  }
  return flush;
}