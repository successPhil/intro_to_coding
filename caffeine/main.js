function drinks(day){
    switch(day){
        case 'm':
        case 'f':
            return 6
        case 'w':
        case 'r':
            return 3
    default:{
        return 4
    }        
    }
}

// Decided to solve this with switch() because
// it does not exist in python, but also to practice
//The reason there are no 'breaks' in my switch()
// is because we are using return which will end the loop
// The other approaches in main.py will also work
console.log(drinks('t')) //  => 6
console.log(drinks('m')) // => 3