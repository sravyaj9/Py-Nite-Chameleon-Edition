# count the occurrence of a number

def count_occurrence( word, x):
    count=0
    for c in word:
        if c==x:
            count+=1
    return count

word=input("enter the word")
x=input("enter the character")
count=count_occurrence(word,x)
print(f"{x} occured {count} times in {word}")



# sum of the digits in a list

def sum_of_numbers(n):
    sum=0
    for i in n:
        sum=sum+i
    return sum
l=input("enter the list of numbers to be added with spaces")
n=list(int(x) for x in l.split(" "))
sum=sum_of_numbers(n)
print(f"sum of the numbers{n} is {sum}")

#sum of the digits in a number
def sum_of_numbers(n):
    sum=0
    while n>0:
        i=n%10
        sum=sum+i
        n=n//10
    return sum
n=int(input("enter the number"))
sum=sum_of_numbers(n)
print(f"sum of the numbers in {n} is {sum}")

# average of the numbers in a list
def avge(l):
    sum=0
    sum_avg=0
    for i in l:
        sum=sum+i
    sum_avg=sum/len(l)
    return sum_avg
l=input("enter the list of numbers to be averaged with space between them")
n= avge(list(int(x) for x in l.split(" ")))
print("average of the numbers is", n)


# The length of each list
def list_length(n):
    length=len(n)
    return length


south=["texas","arizona","california","florida"]
north=["washington","Montana","New York"]
east=["georgia","NJ","DC","philadelphia"]
west=["Oregon","Nevada"]

print("The number of south states are",list_length(south))
print("The number of north states are",list_length(north))
print("The number of east states are",list_length(east))
print("The number of west states are",list_length(west))


# Items in the list printing
def item_list(l):
    for i in l:
        print(i)
l=[1,2,3]
item_list(l)


