def fly_by(lamps, drone)
  lamps[0...drone.length] = 'o' * drone.length
  lamps
end