import os
def clear(): #creating clear function to clear screen continuously
    os.system(  "cls" if os.name=="nt" else "clear"  )
library = {}
def add(): #creating add function for adding new books
    ISBN = input("Enter ISBN ") #creating a variable to store the ISBN
    library [ISBN] = {} #creating the ISBN key in the library dictionary and its type is dictionary
    Title = input("Enter title: ") #creating a variable to store the title of the book
    library [ISBN]["Title"] = Title  #creaeting a key-value pair of the title in the ISBN dictionary
    Author = input("Enter author: ") #creating a variable to store the Author of the book
    library [ISBN]["Author"] = Author #creating a key-value pair of the author of the book in the ISBN dictionary
    library[ISBN]["Available"] = True
    print(f"The Book '{Title}' by '{Author}' added to the catalog with an ISBN = {ISBN}")
    
def get_choice():
    user_choice = input("""
Menu:
1.Add Book
2.Check Out Book
3.Check In Book
4.List Book
5.Exit
Enter your choice (1-5) 
""") #The choice input message
    return user_choice
def check_out():
    ISBN_to_check_out = input("Enter ISBN to check out: ")   
    if ISBN_to_check_out in library:
        if library[ISBN_to_check_out]["Available"] == True:
            library[ISBN_to_check_out]["Available"] = False
            print(f"Book {library[ISBN_to_check_out]['Title']} checked out successfully ")
        else:
            print("Sorry the book is currently checked out ")
    else:
        print("There is no book with such serial number in the library")
def check_in():
    ISBN_to_check_in = input("Enter ISBN of the book to be checked in")
    if ISBN_to_check_in in library :
        if library[ISBN_to_check_in]["Availability"] == False:
            library[ISBN_to_check_in]["Availability"] = True
            print("This book is successfully checked in")
        else:
            print("This book is already in the library")
    else:
        print("This book isn't found in the catalog")
        
while True:
    clear()
    choice = get_choice()
    if choice == "1":
        clear()
        add()
        another = input ("Do you want to add another book? y/n ")
        while another == "y":
            clear()
            add()
            another = input ("Do you want to add another book? y/n ")
        #another = input("Do you want to add another")
    elif choice == "2":
        check_out()
        another = input ("Do you want to check out another book? (y/n): ")
        while another == "y":
            clear()
            check_out()
            another = input("Do you want to check out another book? (y/n): ")
    elif choice == "3":
        clear()
        check_in()
        another = input("Do you want to check in another book? (y/n): ")
        while another == "y":
            clear()
            check_in()
            another = input("Do you want to check in another book? (y/n): ")
    elif choice == "4":
        print(library)
        go_back = input("press Enter to go back to the menu...") 
    elif choice == "5":
        print("Exiting the program")
        break
    else:
        print("Invalid choice")
        input("Press Enter to go back to the main menu....")
    
    
        
            