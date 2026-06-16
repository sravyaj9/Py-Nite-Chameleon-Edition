# Contact book
# adding a contact
contact={}
def add_contact(name, phonenumber):
    if name in contact.keys():
        print("contact already exists")
    else:
        contact[name]=phonenumber
        print(contact)


# search a contact
def search_contact(name):
    for i in contact.keys():
        if i==name:
            print(f"phone number of {name} is", contact[name])
        else:
            print("contact does not exist")



# view all contacts
def view_contacts():
    if contact:
        for name, phonenumber in contact.items():
            print(f"{name}: {phonenumber}")
    else:
        print("no contact")


#delete contacts
def delete_contact(name):
   if name in contact.keys():
        del contact[name]
        print(f"contact {name} is deleted")
def update_contact(name, phonenumber):
    if name in contact:
        contact[name] = phonenumber
        print(f"contact {name} is updated")
while True:
    print("welcome to the phone book")
    print ("enter 1: to add contact")
    print("enter 2: to search contact")
    print("enter 3: to view contacts")
    print("enter 4: to delete contact")
    print("enter 5: to update contact")
    print("enter 6: to exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        name=input("enter the name of the contact")
        phonenumber=int(input("enter the phone number"))
        add_contact(name, phonenumber)
    elif choice==2:
        name=input("enter the name of the contact")
        search_contact(name)
    elif choice==3:
        view_contacts()
    elif choice==4:
        name=input("enter the name of the contact to be deleted")
        delete_contact(name)
    elif choice==5:
        name=input("enter the name of the contact to be updated")
        phonenumber=int(input("enter the phone number"))
        update_contact(name, phonenumber)
    elif choice==6:
        break













