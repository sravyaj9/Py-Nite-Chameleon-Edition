#lambda functions
#program1 : adding two numbers
add=lambda a,b:a+b
print(" addition result using lambda function is :",add(3,4))

#program 2 : square of 2 numbers

square=lambda a:a**2
print("square of a number using lambda function is :", square(5))

#program 3: even or odd

num=int(input("enter a number:"))
if num%2==0:
    print("even number")
else:
    print("odd number")

# even or odd using user defined
num1=int(input("enter a number1:"))
numtype=lambda num1 :"even" if num1%2==0 else "odd"
print(f"number {num1}  from lambda function is:",numtype(num1))

#program 4 : even numbers from a list

a=[2,3,4,5,6]
even_numbers=list(filter(lambda a:a%2==0,a))
print("list of even numbers are :",even_numbers)

#program 5 : return last character using lambda

str="hello"
last=lambda str:str[-1]
print("last character is :",last(str))

#program 6: length of the string using lambda
str=input("enter a string")
length=lambda str:len(str)
print("length of string is :",length(str))

#program 7: cube of the number
num=int(input("enter a number:"))
cube=lambda num: num**3
print("cube of the number from lambda function is :", cube(num))

#program 8: find the maximum of 2 numbers

greatest=lambda a,b:a if a>b else b
print("greatest number between 2 numbers:", greatest(5,6))

#program 9: square root of a number

import math
sqroot=lambda b:math.sqrt(b)
print("square root of a number is:",sqroot(25))

upper=lambda a:a.upper()
print("The capitalized string is :",upper("sravya"))

