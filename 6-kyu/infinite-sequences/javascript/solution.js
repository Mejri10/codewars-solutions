function sequence(fun){
  return {
    take: (num) => {
      const ans = [];
      for (let i = 0; i < num; i++) {
        ans.push(fun(i))
      }
      return ans;
    },
    takeWhile: (predicateFunc) => {
      const ans = [];
      for (let i = 0; predicateFunc(fun(i)); i++) {
        ans.push(fun(i));
      }
      return ans;
    }
  }
}