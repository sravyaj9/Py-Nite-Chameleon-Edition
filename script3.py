# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# amount=float(input('enter the amount spend'))

# if(amount>=3000):
#     discount=amount*0.25
# elif(amount>=2000):
#     discount=amount*0.15
# elif(amount>=1000):
#     discount=amount*0.05
# else:
#     print(" no discount")
# print("the discount amount is : ",discount)
# print("Your total amount payable is:", amount-discount)


#user authentication

# username=input(print("enter your username"))
# password=input("enter your password")
# if(username=='admin' and password=='abcdef'):
#     print("login successful")
# elif(username=='admin'):
#     print("password is incorrect")
# elif(password=='abcdef'):
#     print("username is incorrect")
# else:
#     print("username and password are incorrect")
#

#




# salary=int(input("enter your salary"))
# if(salary<=250000):
#     tax=0
# elif(salary<=500000):
#     tax=salary*0.05
# elif(salary<=1000000):
#     tax=salary*0.20
# else:
#     tax=salary*0.30
# print("your salary is",salary)
# print("your tax is",tax)
# print("your salary after tax is",salary-tax)



# subscribers=int(input(" enter the number of subscribers"))
# watch_hours=int(input(" enter the number of watch hours"))
# if(watch_hours>=4000 and watch_hours<10000 and subscribers<5000 and subscribers>=1000):
#     print("your channel is monetized")
#     amount_recd=watch_hours*0.05
#     print("you will receive:",amount_recd)
# elif(watch_hours>=10000 and subscribers>=5000):
#         print("your channel is monetized")
#         amount_recd=watch_hours*0.10
#         print("you will receive:",amount_recd)
# else:
#     print("your channel is not monetized yet")



# gender=input("enter your gender")
# age=int(input("enter your age"))
# is_vehicle=bool(input("do you have a bike?enter True if you don't have a bike, enter False if you have a bike"))
# if gender=="male":
#     if age>=20:
#         if is_vehicle==True:
#             print(" you are eligible for job")
#         else:
#             print(" you are not eligible for job as you don't have a bike")
#     else:
#         print("age must be greater than 20")
# else:
#     print(" you must be male to be eligible for the job")


# driving license eligibility

# age=input("enter your age")
# test= input("did you pass the test yes/no")


#online shopping

#method 1
# amount=int(input("enter the amount spent in amazon shopping:"))
# is_prime=input("are you having a prime membership yes/no:")
# if amount>=1000:
#     print("you are eligible for free delivery")
# elif amount<=1000:
#     if is_prime=="yes" :
#         print("you are eligible for free delivery")
#     else:
#          print("delivery charges applicable,subscribe to prime for free delivery")
#
#method 2
# amount=int(input("enter the amount spent in amazon shopping:"))
# is_prime=input("are you having a prime membership yes/no:")
# if(amount>=1000 or is_prime=="yes"):
#     print("you are eligible for free delivery")
# else:
#     print("delivery charges applicable,subscribe to prime for free delivery")




# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# print( "Sum of those 2 numbers is:", a+b)

# sum=0
# for i in range(1,10,1)
#     sum=sum+i
#     print(sum)
# print(" list of odd numbers are:")
# for i in range(1,11):
#     if(i%2==1):
#         print(i)
#
# print(" Sum of even numbers is :")
# sum=0
# for i in range(1,11):
#     if(i%2==0):
#         sum=sum+i
# print(sum)

#sum of odd numbers
# print("sum of odd numbers is:")
# sum=0
# for i in range(1,10):
#     if(i%2==1):
#         sum=sum+i
# print(sum)


#multiplication table

# print("The multiplication table for the given number is:")
# prod=1
# n=int(input(" Enter the number for which you want to find the multiplication table:"))
# for i in range(1,11):


#fibonaccii sequence
# a=0
# b=1
# for i in range(1,10):
#     c=a+b
#     print(c)
#     a=b
#     b=c
# reverse order
# for i in range(5,0,-1):
#     print(i)


# while loop

# i = 1
# while i <= 10:
#     if i == 3:
#         i = i + 1
#         continue
#     print(i)
#     i = i + 1


# i=1
# while(i<=10):
#     if(i==3):
#         break
#     print(i)
#     i=i+1
# i = 0
# while i < 6:
#     i += 1
#
#     if i % 2 == 0:
#         continue   # skip even numbers
#
#     print("Odd:", i)
#
# text="hello"
# i=0
# while(i<len(text))


#cash withdrawal
#cash deposit
#check  balance
pin=1234
balance=12000
user_pin=int(input("enter your pin:"))
if(user_pin==pin):
    while True:
        print("welcome to ATM stimulator")
        print("1:Check balance")
        print("2:Withdraw")
        print("3:Deposit")
        print("4:Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            print("Balance in your account is",balance)
        elif choice==2:
            amount=int(input("Enter the amount you want to withdraw:"))
            if(amount<balance):
                balance=balance-amount
                print("The remaining balance is",balance)
            else:
                print("insufficient balance")
        elif choice==3:
            amount=int(input("Enter the amount you want to deposit:"))
            balance+=amount
            print("The remaining balance is",balance)
        elif choice==4:
            print("Thank you for using ATM simulator")
            break
        else:
            print("please enter from 1-4")
else:
    print("Invalid pin")



#Rock paper scissors



