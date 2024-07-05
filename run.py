def run():

  bookArchives = []
  choice = 0 

  while choice != 4:
    print("Welcome to the Book Archives")
    print("1. Add a new book")
    print("2. Find a book")
    print("3. Display all books")
    print("4. Exit")
    choice = int(input())

    if choice == 1: 
       print("Adding a new book")
       title = input("Enter book title: ")
       author = input("Enter name of author: ")
       genre = input("Enter book genre: ")
       bookArchives.append([title, author, genre])

    elif choice == 2: 
        print("Finding a book")
        searchTerm = input("Find the book you are looking for: ")
        for book in bookArchives:
          if searchTerm in book:
            print(book)
        
    elif choice == 3: 
        print("Displaying all books")
        for book in bookArchives:
           print(book)

    else: 
        choice == 4
        print("Exiting program")

  print("You have successfully exited the program!")

if __name__ == "__main__":
    run()

