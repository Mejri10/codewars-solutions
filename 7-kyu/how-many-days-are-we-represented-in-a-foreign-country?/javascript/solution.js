function daysRepresented(trips) {
    return trips
      .reduce((set, [arrival,  departure]) => {
          for (let i = arrival; i <= departure; i++) {
            set.add(i);
          }
          
          return set;
        },
        new Set()
      )
      .size;
}