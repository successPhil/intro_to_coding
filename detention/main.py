# def haveDetention(id):
#     import re
#     digs = r"\d"
#     highest = max(re.findall(digs, id))
#     if highest == '5' or highest == '6':
#         return True
#     return False



#Solved using regex for practice
#Remember to import re when using python
# findall() syntax is re.findall(regex, str)
#Since regex can be confusing and hard to read,
#Lets use an alternative approach



print(haveDetention("1gh3btsduv6")) #  ==> true
print(haveDetention("1gh3btsduv67")) #  ==> false