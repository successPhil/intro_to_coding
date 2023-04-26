def weightOnX(accOnX, weightOnEarth):
    xweight = (weightOnEarth / 9.8) * accOnX
    if xweight.is_integer():
        return int(xweight)
    return xweight

#Added if statement to check if number can be
#converted to an integer before returning
#if not we return a float
print(weightOnX(9.8, 20056)) # ==> 20056
print(weightOnX(10, 10780))  # ==> 11000