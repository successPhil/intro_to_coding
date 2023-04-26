def illegalWord(sentence, word):
    return word.lower() in sentence.lower()


print(illegalWord('Hello there', 'fudge')) # => false
print(illegalWord("But I didn't say fudge", 'fudge')) # => true
print(illegalWord("But I didn't say fudge", 'Fudge')) # => true