function illegalWord(sentence, word){
    return sentence.toLowerCase().includes(word.toLowerCase())
}


console.log(illegalWord('Hello there', 'fudge')) // => false
console.log(illegalWord("But I didn't say fudge", 'fudge')) //  => true
console.log(illegalWord("But I didn't say fudge", 'Fudge')) //  => true