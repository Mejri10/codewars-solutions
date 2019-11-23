const isOnline = ({status, lastActivity}) => status === 'online' && lastActivity <= 10;
const isAway = ({status, lastActivity}) => status === 'online' && lastActivity > 10;
const isOffline = ({status}) => status === 'offline';

const whosOnline = friends => {
  return friends.reduce((ans, friend) => {
    if (isOnline(friend)) {
      ans.online = ans.online || []
      ans.online.push(friend.username);
    } else if (isOffline(friend)) {
      ans.offline = ans.offline || []
      ans.offline.push(friend.username);
    } else if (isAway(friend)) {
      ans.away = ans.away || []
      ans.away.push(friend.username);
    }
    return ans;
  }, {})
}