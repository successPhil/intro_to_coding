// function alphabetCode(letter){
//     if (letter.charCodeAt(0) >= 65 && letter.charCodeAt(0) <= 90){
//         return letter.charCodeAt(0) - 64
//     }
// }

// alternative solution using a loop

function alphabetCode(letter){
    let alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for (let i = 0; i < alpha.length; i++){
        if (alpha[i] == letter){
            return i + 1
        }
    }
}

console.log(alphabetCode('A'))
console.log(alphabetCode('Q'))
console.log(alphabetCode('T'))
console.log(alphabetCode('Z'))

//Using an object to map values also works in js
// It works very similarly to the example in main.py