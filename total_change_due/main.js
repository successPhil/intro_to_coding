function totalChange(amountPaid, totalCost) {
    let change = amountPaid - totalCost
    return +(amountPaid - totalCost).toFixed(2)
  }
  
  // ---- TESTS - don't change these ---- //
  console.log(totalChange(100, 75) === 25)
  console.log(totalChange(10, 7.28) === 2.72)