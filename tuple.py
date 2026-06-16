#representing tuple
tu=(1,2,3)
print(tu)
# single element
tu=(1)
print(type(tu))
tu=(1,)
print(type(tu))
#multiple data types collection
tu=("sravya",10.5,23,'a',"deepak")
print(tu)
# we can even represent tuple without ()
tu=23,34,45,56,64
print(type(tu))
# accessing elements from the tuple
print("first index number is",tu[0])
print("last index number is ",tu[-1])
print("last index number is ",tu[len(tu)-1])

#slicing the tuple
tu=("sravya",10.5,23,'a',"deepak",23,34,45,56,64)
print("accessing elements from 2nd to 5th index",tu[2:5])
print("accessing elements upto 5th element",tu[:5])
print("accessing elements from 5th element to last",tu[5:])
print("accessing every alternate element in the tuple",tu[::2])
print("accessing elements in the reverse order",tu[::-1])

# tuples are immutable elements
# But we can concatenate two tuples and create another tuple
t1=91,23,3,34,35
t2=98,45
t3=t1+t1
print(t3)
print(type(t3))
# repetition
t3=t1*3
print(t3)
print(type(t3))
#count of 34 in t3
print("34 is there",t3.count(34),"times in the tuple")
# index of 34 in t3
print("34 is present at",t3.index(34),"th position in the tuple")
#packing
t1=(12,23,24)
#unpacking
a1=12
a2=23
a3=24
print(a1)
print(a2)
print(a3)