choice = ""
contacts = {}

while choice != "4":

    choice = input("""Contact management
    
    1-Add a contacet
    2-View contact
    3-Edit a contact
    4-exit

    please choose a number from 1-4
    """)

    if choice == "1":
        ID = input("  Enter the contact ID ")
        contacts [ID] = {}
        name = input(" Enter a name ")
        contacts[ID]["name"] = name

        phone_number = input("Enter a phone number ")
        contacts[ID]["Phone_number"] = phone_number

        while not phone_number.isdigit():
            print("You may entered nondigit character, reenter the correct phone number please")
            contacts ["Phone_number"] = phone_number
        else:
            print(contacts[ID].get("name"),"was added successfully✅✅")

    elif choice == "2":
        print(contacts)

    elif choice == "3":
        ID_to_edit = input("Please enter an ID edit")

        if ID_to_edit in contacts.Keys():
            contacts[ID_to_edit]["Name"] = input("  Eneter a new name ")
            contacts["phone number"] = input("  Please type a new phone number ")
            while not contacts["phone number"].isdigit():
                print("OOPS! You entered non digit phone number")
                contacts["phone number"] = input("  Please type a phone number ")
            print("Success....")

        else:
            print("This ID isn't in the contacts")

    elif choice != "4":
        print("invalid choice, try again")
else:
    print("Exiting the program......")
