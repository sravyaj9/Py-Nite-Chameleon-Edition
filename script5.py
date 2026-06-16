# login system
def login_system(username,password):
    if username == "admin" and password == "adm@123":
        print("Login Successful")
    else:
        print(" either username or password is incorrect")
username=input("Enter your username: ")
password=input("Enter your password: ")
login_system(username,password)

