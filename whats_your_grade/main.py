def myGradeIs(GPA):
    if GPA == 4:
        return 'A'
    elif GPA == 3:
        return 'B'
    elif GPA == 2:
        return 'C'
    elif GPA == 1:
        return 'D'
    return 'F'

print(myGradeIs(4)) # => 'A'
print(myGradeIs(3)) # => 'B'
print(myGradeIs(2)) # => 'C'
print(myGradeIs(1)) # => 'D'
print(myGradeIs(0.9)) # => 'F'

#Note the problem did not specify a range so we did not use one