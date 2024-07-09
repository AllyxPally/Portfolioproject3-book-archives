def get_valid_input(prompt):
    while True:
        try:
            value = input(prompt)
            if not value.strip():
                raise ValueError("Input cannot be empty.")
            return value
        except ValueError as e:
            print(e)

def run(): 
      searchTerm = ""
      bookArchives = []
      choice = 0
      found = False


      while choice != 4:
        print("Welcome to the Book Archives")
        print("1. Add a new book")
        print("2. Find a book")
        print("3. Display all books")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice:\n "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue        
        
        if choice == 1: 
            print("Adding a new book")
            title = get_valid_input("Enter book title: ")
            author = get_valid_input("Enter name of author: ")
            genre = get_valid_input("Enter book genre: ")
            bookArchives.append([title, author, genre])        
        
        elif choice == 2: 
            print("Finding a book")
            searchTerm = get_valid_input("Find the book you are looking for: ")
            found = False

            for book in bookArchives:
                    if searchTerm.lower() in (field.lower() for field in book):
                        print(book)
                        found = True
            if not found: 
                print("No book found with that term.\n")        
        
        elif choice == 3: 
                print("Displaying all books")
                if bookArchives:
                    for book in bookArchives:
                        print(book)
                        
                else:
                    print("No books in the archive.\n")  
                     
                    
       
        elif choice == 4:
                print("Exiting program....")
                print("You have successfully exited the program!")
        else:
         print("Please enter a valid choice.")    
       
           
if __name__ == "__main__":
  run()