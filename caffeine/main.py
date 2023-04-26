# import math
# def drinks(day):
#     if day == 'm':
#         return math.ceil(800/150)
#     elif day == 't':
#         return math.ceil(600/150)
#     elif day == 'w' or day == 'r':
#         return math.ceil(400/150)
#     elif day == 'f':
#         return math.ceil(900/150)
    

#Above code makes use of if else statements.
#Another thing to note we can calculate our
#minimum values prior to writing our code
#For example:
def drinks(day):
    # caffGenerator = {
    #     'm': 6,
    #     't': 4,
    #     'w': 3,
    #     'r': 3,
    #     'f': 6
    # }
    # return caffGenerator[day]
    if day == 'm' or day == 'f':
        return 6
    elif day == 'w' or day == 'r':
        return 3
    return 4


#Seeing the values like this makes it easier to see
#That we can combine if/else or keys to shorten code


print(drinks('m')) #  => 6
print(drinks('r')) #  => 3