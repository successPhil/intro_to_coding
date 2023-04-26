function weightOnX(accOnX, weightOnEarth){
    return (weightOnEarth / 9.8) * accOnX
}


console.log(weightOnX(9.8, 20056)) // ==> 20056
console.log(weightOnX(10, 10780)) // ==> 11000