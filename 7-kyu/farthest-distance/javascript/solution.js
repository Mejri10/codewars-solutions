function furthestDistance(arr){
   let maxDistance = 0;
   arr.forEach(([xi, yi]) => {
     arr.forEach(([xj, yj]) => {
       const distance = Math.hypot(xj - xi, yj - yi);
       if (distance > maxDistance) {
         maxDistance = distance;
       }
     })
   })
   return parseFloat(maxDistance.toFixed(2));
}