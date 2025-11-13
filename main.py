from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

def available(books):
    available_books = []
    for book in books:
        if book['available']:
            available_books.append(book)
            print(f"{book['id']}: {book['title']} by {book['author']}")
    if len(available_books) == 0:
        print('No books are available')


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search(books):
    ans = input("Enter the name of the author, or the genre you are looking for: ").lower()
    
    matches = []
    for book in books:
        if book['author'].lower() == ans or book['genre'].lower() == ans:
            matches.append(book)
        else:
            continue
    
    return matches


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout(books):
    available(books)
    ans = input("Enter the ID of the book you'd like to check out: ")
    for book in books:
        if book['id'] == ans:
            if book['available'] == False:
                print(f"{book['id']} is not available")
                return
            book['available'] = False
            due = datetime.today() + timedelta(weeks = 2)
            book['due_date'] = due.strftime("%Y-%m-%d")
            book['checkouts'] += 1
            print(f"You checked out {book['title']}. Due Date: {book['due_date']}")
            return
    print('No book found with that id')


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_book(books):
    ans = input("Enter the ID of the book you'd like to return: ")
    for book in books:
        if book['id'] == ans:
            if book['available'] == True:
                print(f"{book['id']} is already available")
                return
            book['available'] = True
            book['due_date'] = None
            print(f"You returned {book['title']}.")
            return
    print('No book found with that id')

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def overdue(books):
    today = datetime.today().date()
    print("The following books are overdue: ")
    found = False
    for book in books:
        if book['due_date'] is None:
            continue

        due = datetime.strptime(book['due_date'], "%Y-%m-%d").date()
        if book['available'] == False and due < today:
            print(f"{book['id']}: {book['title']} was due on {book['due_date']}")
            found = True

    if found == False:
        print('No books are overdue')

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    available(library_books)
    print(search(library_books))
    print(checkout(library_books))
