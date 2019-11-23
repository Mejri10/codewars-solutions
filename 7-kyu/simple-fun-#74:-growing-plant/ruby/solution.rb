def growing_plant(upSpeed, downSpeed, desiredHeight)
  upSpeed >= desiredHeight ?
    1 :
    1 + growing_plant(upSpeed, downSpeed, desiredHeight - (upSpeed - downSpeed))
end