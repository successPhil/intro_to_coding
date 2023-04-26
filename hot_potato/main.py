def potato(turn):
    order = [2, 3, 4, 0, 1]
    return order[turn % 5]

print(potato(0)) #  => 2
print(potato(1)) #  => 3
print(potato(7)) #  => 4

# Note using mod length of the array guarantees
#no matter what number we get for turn we will get
#a valid index in our array