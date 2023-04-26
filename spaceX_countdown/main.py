def countDown(num):
    while num >= 0:
        print(f"There are {num} seconds left until lift off!")
        num -=1
    return "Lift Off!"

print(countDown(5))