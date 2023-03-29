'''The program is a simple phonebook that allows adding, removing,
editing and displaying all stored contacts'''

phoneBook = {}

while True:
    print("--------------------------------------------------------------")
    print("Please choose one of the following options: ")
    print("a - Add a new contact")
    print("b - Get a contact's details")
    print("c - Remove a contact")
    print("d - Display all the contacts")
    print("e - Exit")
    option = input("Please enter an option: ")

    if(option == "a"):
        name = input("Enter contact name: ")
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email: ")
        phoneBook[name] = [phone, email]
        print("Contact has been added")

    if(option == "b"):
        name = input("Enter the name of the contact to display: ")
        contact = phoneBook[name]
        print("Name:", name,  "Phone:", contact[0], "Email:", contact[1])

    if(option == "c"):
        name = input("Enter the name of the contact to remove: ")
        del phoneBook[name]
        print("Contact has been removed")

    if(option == "d"):
        for name, contact in phoneBook.items():
            print("Name:", name, "Phone:", contact[0], "Email:", contact[1])

    if(option == "e"):
        break
