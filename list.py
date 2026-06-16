
var=[1,2,3,4,5,6]
print(var)
#duplicates
var1=list[1,2,5,5,4,5,6]
print(var1)
#multiple data type
var2=list['sravya',95,96, 94.5,"Akshat"]
print(var2)
#nested list
var3=[[1,2,3],[4,5,6],[7,8,9],3,4,5]
print(var3[0][1])
print(var3[1][1])
print(var3[2][1])
print(var3[-1])
print(var3[-4][-1])
print(var3[len(var)-1])

#modification
#removes last value
var3.pop()
print(var3)
#removes that particular value
var3.remove(4)
print(var3)
#appends that value at the end
var3.append("Devansh")
print(var3)
#insert that value at that index
var3.insert(4,10)
print(var3)
#updating a particular value in the list
var3[1]="Akshat"
print(var3)
#removes the value at first index
var3.pop(1)
print(var3)
#printing the values in the list
for i in var3:
    print(i)
var4=[2,4,6,7,8,8,8, 34,58]
#checking if 6 is present in the list
if 6 in var4:
    print(" 6 is present in the list")
else:
    print("6 is not present in the list")
#checking if a number is present in the list at runtime
a=int(input("Enter a number to check if it is present in the list"))
if a in var4:
    print(f"number {a} is present in the list")
else:
    print(f"number {a}  is not present in the list")
#reversing a list
var4.reverse()
print(var4)
#knowing the length of the list
print("length of list", len(var4))
#finding out at which index a particular value is present
print("6 is present in ",var4.index(6),"this position")
#reversing a string
var4.reverse()
print(var4)
#sort from small to big
#method1
var4.sort()
print(var4)
#method2
a=sorted(var4)
print("the ascending order of the list is", a)
#sort from big to small
#method1
var4.sort(reverse=True)
print("the descending order of the list is:",var4)
#method2
b=sorted(var4, reverse=True)
print("descending order:", b)

#finding out a particular string is present in the list/online movie recommendation
movie_list=["mirai","nari nari naduma murari", "mana shakara varaprasad","girl friend"]
movie=input("enter the movie name you want to search for")
if movie in movie_list:
    print(f"{movie} is in the list")
else:
    print(f"{movie} is not in the list")

#online shopping cart

cart=[]
price=[]

# add to cart
cart.append("frock")
price.append(3200)
cart.append("shoes")
price.append(5000)
cart.append("bag")
price.append(1000)
print("Items added to the cart are:",cart)
print("price of the cart:",sum(price))

#delete an item in the cart
remitem=input("enter the item you want to remove from the cart ")
if remitem in cart:
    rem=cart.index(remitem)
cart.pop(rem)
price.pop(rem)
print("updated cart items are:",cart)
print("update bill is ", sum(price))














