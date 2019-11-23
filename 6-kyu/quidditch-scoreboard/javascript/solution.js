const VALID_ACTIONS = {
  "Quaffle goal": 10,
  "Caught Snitch": 150,
  "Blatching foul": -30,
  "Blurting foul": -30,
  "Bumphing foul": -30,
  "Haverstacking foul": -30,
  "Quaffle-pocking foul": -30,
  "Stooging foul": -30
}

function parseTeams(teams) {
  return teams.split(' vs ');
}

function parseActions(actions) {
  return actions.split(', ').map(parseAction);
}

function parseAction(action) {
  const [team, value] = action.split(': ');
  return { team, value };
}

function formatScore(score) {
  return Object
          .keys(score)
          .reduce((scores, team) => {
            scores.push(`${team}: ${score[team]}`);
            return scores;
          }, [])
          .join(", ");
}

function quidditchScoreboard(teams, actions) {
  const teamNames = parseTeams(teams);
  const score = teamNames.reduce((current_score, team) => {
    current_score[team] = 0;
    return current_score;
  }, {})
  for ({team, value} of parseActions(actions)) {
    score[team] += VALID_ACTIONS[value];
    if (value === "Caught Snitch") break;
  }
  return formatScore(score);
}