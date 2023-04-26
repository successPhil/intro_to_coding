function removeZeros(num){
    return Number(num.toString().replaceAll('0', ''))
}

// Above is replace solution
// Below is regex solution
// function removeZeros(num){
//     let regEx = /[1-9]/g
//     let nonZero = num.toString().match(regEx).join('')
//     return Number(nonZero)
// }

console.log(removeZeros(1001)) // => 11
console.log(removeZeros(50680019)) // => 56819