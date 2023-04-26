def totalChange(amountPaid, totalCost):
    change = amountPaid - totalCost
    return round(change, 2)

# ---Tests-- Do not change ---
print(totalChange(100, 75) == 25)
print(totalChange(10, 7.28) == 2.72)