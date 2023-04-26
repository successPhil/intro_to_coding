function mortgagePayment(amountInvested, annualInterest){
    return Number(amountInvested * annualInterest)
}




console.log(mortgagePayment(100000,.05)) // => 5000
console.log(mortgagePayment(15000,.085)) // => 1275