function countDown(num){
    while (num >= 0){
        console.log(`There are ${num} seconds until lift off!`)
        num --
    }
    return "Lift Off!"
}
console.log(countDown(5))