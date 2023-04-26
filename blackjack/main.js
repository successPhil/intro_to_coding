function blackjack(num){
    switch(true){
        case (num > 21):
            return 'bust'
        case (num < 15):
            return 'hit'
    default:{
        return 'stand'
    }
    }
}
//Using switch again for practice
//Notice this time the expression we eval is true
// this way we can give expressions to check and execute if true
// and our default handles if no cases are true

console.log(blackjack(5)) // => 'hit'
console.log(blackjack(20)) // => 'stand'
console.log(blackjack(23)) // => 'bust'