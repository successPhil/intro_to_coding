def blackjack(num):
    if num > 21:
        return 'bust'
    elif num < 15:
        return 'hit'
    else:
        return 'stand'
    
print(blackjack(5)) # => 'hit'
print(blackjack(20)) # => 'stand'
print(blackjack(23)) # => 'bust'