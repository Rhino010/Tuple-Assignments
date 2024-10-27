"""
2. Python Data Structure Challenges in Real-World Scenarios
Task 1: Library System Enhancement Sharpen your skills in 
    managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where each 
book is stored as a tuple within a list. Your task is to update 
this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
- Add functionality to insert new books into `library`. Ensure that adding 
a duplicate book is handled appropriately.
"""

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):
    found = False
    new_title = input("Please enter the title of the book:\n")
    new_author = input("Plese enter the author's name:\n")
    new_book = (new_title, new_author)
    for title, author in library:
        if new_title.lower() == title.lower():
            found = True
    if found == False:
        library.append(new_book)
        print(f"{new_title} by {new_author} has been added to the library.")
    elif found == True:
        print("Book already exists.")

while True:
    print("\n1. Add a book\n2. Show the library\n3. Quit")
    choice = input("Please make a selection from the above list.\n")
    
    if choice == '1':
        add_book(library)
    elif choice == '2':
        print(library)
    elif choice == '3':
        print('Exiting program.......')
        break
    else:
        print("Invalid option please try again.")

    