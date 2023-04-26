function potato(turn){
    let order = [2, 3, 4, 0, 1]
    return order[turn % 5]
}




console.log(potato(0)) // => 2
console.log(potato(1)) // => 3
console.log(potato(7)) // => 4