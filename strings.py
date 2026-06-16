#strings

print('a') # single character
print("ab") # string
print('hello world')# single quotes string
print("hello world") # double quotes string
print('''hello world''') # triple single quotes string
print("""hello world""") # triple double quotes string

# access the strings
var="Hello world"
print(var[0])
print(var[4])
print(var[len(var)-1])

# accessing strings in the reverse order
print(var[-1])
# slicing
print(var[5:11])
#By default accessing first index number/accesing all the elements from starting to that particular index
print(var[:5])
#accessing all the elements from that particular index to the last by default
print(var[6:])
# accesing the elements in reverse order
print("reverse order:",var[::-1])
#accesing every 2nd index number
print("every second index number:",var[::2])


#
