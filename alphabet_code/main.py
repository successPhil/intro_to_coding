def alphabetCode(letter):
    if ord(letter) >= 65 and ord(letter) <= 90:
        return ord(letter) - 64
# print(alphabetCode('A'))
# print(alphabetCode('Q'))
# print(alphabetCode('Z'))
# print(alphabetCode('J'))

#above we used ord() to get the ascii code of our input
# Letters A-Z are code 65-90, -64 is 1-26

#This problem can also be solved using an object of
#key value pairs i.e ('A': 1, 'B': 2...)

# def alphabetCode(letter):
#     values = {
#         'A': 1,
#         'B': 2,
#         'C': 3,
#         'D': 4,
#         'E': 5,
#         'F': 6,
#         'G': 7,
#         'H': 8,
#         'I': 9,
#         'J': 10,
#         'K': 11,
#         'L': 12,
#         'M': 13,
#         'N': 14,
#         'O': 15,
#         'P': 16,
#         'Q': 17,
#         'R': 18,
#         'S': 19,
#         'T': 20,
#         'U': 21,
#         'V': 22,
#         'W': 23,
#         'X': 24,
#         'Y': 25,
#         'Z': 26
#     }
#     return values[letter]

#While hard to observe here, these are very efficient
#operations. Because our value is mapped we are not looping
# or iterating through anything. We can instantly return the
#value in close to constant time

#Another alternative approach that is not as
#efficient but is easy to understand is the loop
#we can create a string of all of our uppercase letters
#and return the index + 1 for the letter entered into the function.


# def alphabetCode(letter):
#     alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for i, char in enumerate(alpha):
#         if char == letter:
#             return i + 1
        
print(alphabetCode('A'))
print(alphabetCode('Q'))
print(alphabetCode('Z'))
print(alphabetCode('J'))
        

