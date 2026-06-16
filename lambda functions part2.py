# program 1 : convert all the element in a list to upper case
var=["sravya","Deepak","Akshat","Devansh"]
upper_case= list(map(lambda var:var.upper(),var))
print(upper_case)

# program 2: To print only elements starting with letter 'D'
var=["sravya","Deepak","Akshat","Devansh"]
dstart=list(filter(lambda var:var.startswith('D'),var))
print(dstart)

#program 3: multiply three numbers

product=lambda a,b,c:a*b*c
print("Product of three numbers:",product(2,3,4))


#program 4: multiply the numbers in the list
import math

from functools import reduce
var=[1,2,3,4,5]
prod=math.prod(var)
print(prod)
mult=reduce(lambda x,y:x*y,var)
print(mult)



