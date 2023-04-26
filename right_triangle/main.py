def rightTriangle(base, height):
    area = 1/2 * base * height
    if area.is_integer():
        return int(area)
    
    return area

print(rightTriangle(2, 2) == 2) # => 2
print(rightTriangle(1, 1) == 0.5) # => 0.5

# print(area.is_integer()) checks whether the float
#value is an integer or not and returns bool