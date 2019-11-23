function getSectionIdFromScroll(scrollY, sizes) {
   return (
     sizes
       .reduce((secs, size, idx) => {
           secs.push(size + (secs[idx-1] || 0))
           return secs;
         },
         []
       )
       .findIndex(sec => scrollY < sec)
   );
}