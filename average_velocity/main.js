function avgVel(posArr, time){
    vel = (posArr[posArr.length-1] - posArr[0]) / time
    return vel
}

console.log(avgVel([0, 4, 6], 10)) // => 0.6
console.log(avgVel([3, 2, 7], 4)) // => 1