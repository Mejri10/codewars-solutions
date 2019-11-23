function scoreCalculator([score, catchSnitch]) {
  return score + (catchSnitch === 'yes' ? 150 : 0);
}

function gameWinners(gryffindor, slytherin) {
    const gryffindorPoints = scoreCalculator(gryffindor);
    const slytherinPoints = scoreCalculator(slytherin);
    if (gryffindorPoints > slytherinPoints) {
      return "Gryffindor wins!";
    } else if (gryffindorPoints < slytherinPoints) {
      return "Slytherin wins!"
    } else {
      return "It's a draw!";
    }
};