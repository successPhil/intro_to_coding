def fizzBuzz(num):
    answer = {}
    start = 1
    while start <= num:
        if start % 15 == 0:
            answer[start] = 'FizzBuzz'
        elif start % 5 == 0:
            answer[start] = 'Buzz'
        elif start % 3 == 0:
            answer[start] = 'Fizz'
        else:
            answer[start] = start
        start += 1
    
    return answer
print('hello')
print(fizzBuzz(100))
