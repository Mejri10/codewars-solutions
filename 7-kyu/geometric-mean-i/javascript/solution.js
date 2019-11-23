function geometricMeanI(arr){ 
    const arrFiltered = arr.filter(n =>
      typeof n === 'number' && n >= 0
    )
    
    const numberOfInvalidEntries = arr.length - arrFiltered.length;

    if (arr.length < 11 && numberOfInvalidEntries > 1 || 
        arr.length >= 11 && numberOfInvalidEntries >= arr.length * 0.1) {
        return 0;
    }
    
    return Math.pow(
      arrFiltered.reduce((prod, n) => prod * n, 1),
      1/arrFiltered.length
    );
}