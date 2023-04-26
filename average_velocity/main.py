def avgVel(posArr, time):
    vel = (posArr[-1] - posArr[0]) / time
    if vel.is_integer():
        return int(vel)

    return vel

print(avgVel([0, 4, 6], 10)) # => 0.6
print(avgVel([3, 2, 7], 4)) # => 1

#If we do not call int() on vel, we will return
#float numbers i.e (1.0 instead of 1)