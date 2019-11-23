function queueTime(customers, n) {
  if(customers.length === 0) return 0;
  
  let totalTime = 0;
  let customersBeingServed = customers.slice(0, n);
  let customersLeftInQueue = customers.slice(n);
  customersLeftInQueue.forEach(customer => {
      const lowest = Math.min(...customersBeingServed);
      const lowestIdx = customersBeingServed.findIndex(c => c === lowest);
      customersBeingServed = customersBeingServed.map(c => c - lowest);
      customersBeingServed[lowestIdx] = customer;
      totalTime += lowest;
  });
  totalTime += Math.max(...customersBeingServed);
  return totalTime;
}