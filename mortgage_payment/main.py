def mortgagePayment(amountInvested, annualInterest):
    return int(amountInvested * annualInterest)




print(mortgagePayment(100000,.05)) # => 5000
print(mortgagePayment(15000,.085)) # => 1275