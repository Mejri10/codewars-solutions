def evaporator(content, evap_per_day, threshold)
  (Math.log(threshold/100.0)/Math.log(1-evap_per_day/100.0)).ceil
end