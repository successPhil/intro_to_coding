def removeZeros(num):
   test = str(num).replace('0', '')
   return int(test)

# First solution above
#Regex solution below for practice
# import re
# def removeZeros(num):
#     regex = r'[1-9]'
#     notZero = re.findall(regex, str(num))
#     return int(''.join(notZero))

print(removeZeros(5005))
print(removeZeros(50680019))
