function fizzBuzz(num){
    let answer = {}
    let start = 1
    while (start <= num){
        if (start % 15 == 0){
            answer[start] = 'FizzBuzz'
        }
        else if (start % 5 == 0){
            answer[start] = 'Buzz'
        }
        else if (start % 3 == 0){
            answer[start] = 'Fizz'
        }
        else{
            answer[start] = start
        }
        start ++
    }
    return answer
}

console.log(fizzBuzz(100))