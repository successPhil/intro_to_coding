function myGradeIs(GPA){
    switch(GPA){
        case 4:
            return 'A'
        case 3:
            return 'B'
        case 2:
            return 'C'
        case 1:
            return 'D'
    default:{
        return 'F'
    }
    }
}

console.log(myGradeIs(4))
console.log(myGradeIs(3))
console.log(myGradeIs(2))
console.log(myGradeIs(1))
console.log(myGradeIs(0.9))

// We used switch() again, I like to practice it
// When using js to remember the syntax
// Remember that we do not need to break for any of
// our switch cases because we are using 'return'
// If instead we were to update a value and continue checking
// Other cases, we would update our variable and use break instead of return
