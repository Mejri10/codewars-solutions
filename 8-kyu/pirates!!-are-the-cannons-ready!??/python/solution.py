def cannons_ready(gunners):
  if len(gunners) == gunners.values().count('aye'):
      return 'Fire!'
  else:
      return 'Shiver me timbers!'