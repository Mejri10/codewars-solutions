const wave = str =>
  str.split('').reduce((arr, c, idx) =>
    c.match(/[a-z]/) ?
      [...arr, str.slice(0, idx) + c.toUpperCase() + str.slice(idx+1)] :
      arr
  ,[])