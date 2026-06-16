# Functions
def add(a,b) :
    c=a+b
    return c
sum=add(10,20)
print("sum is :", sum)

#calculator
def calc(a,b) :
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum, sub,mul, div

s,su,mul, div= calc(10,20)
print("sum is ", s)
print(" difference is ",su)
print("product is ",mul)
print("division is ",div)

#check even or odd using functions

def even(a) :
    if a%2==0:
        return "even"
    else:
        return "odd"
num= even(int(input("enter a number")))
print("entered number is",num )

# palindrome

def palindrome(word):
    if(word==word[::-1]):
        return"palindrome"
    else:
        return "not palindrome"
s=palindrome(input("enter a word"))
print("The word is", s)

#using true or false

def is_palindrome(word):
    if(word==word[::-1]):
        return True
    else:
        return False
word=input("enter a word")
if is_palindrome(word):
    print("It is a palindrome",word)
else:
    print("Not a palindrome",word)

# reverse of a string

def reverse(s):
    return(s[::-1])
s=input("enter a word to reverse")
rev=reverse(s)
print(f"The reverse of the word {s}  is", rev)

# max of 3 numbers

import math
def find_max(a,b,c):
    return max(a,b,c)

maxi=find_max(4,5,6)
print("The highest number is ",maxi)



