'''
Implement a student library system using OOPs 
where students can borrow books from a list of books.
Create a separate student and library class. 
Program must be menu-driven.
'''

# book1 = "Warriors"
# book2 = "The School for Good and Evil"
# book3 = "The Lost Rainforest"
# book4 = "Wild Rescuers"
# book5 = "Five Elements"
# book6 = "Omega City"
# book7 = "Wing & Claw"
# book8 = "The Copernicus Legacy"
# book9 = "The Thickety"
# book10 = "The Doldrums"

book_lib = {
    "book1" : 's', "book2" : 's', "book3" : 's', "book4" : 's', "book5" : 's',
    "book6" : 's', "book7" : 's', "book8" : 's', "book9" : 's', "book10" : 's'
    }

# The book_lib is the main dictionary here. 
# We update it regularly to determine whether a particular book is present in the library or not. 
# 's' states that the book is present and 't' states that the book is not present. 

while True :

    print('''
    The Books in the Library are as follows :

    book1 = "Warriors"
    book2 = "The School for Good and Evil"
    book3 = "The Lost Rainforest"
    book4 = "Wild Rescuers"
    book5 = "Five Elements"
    book6 = "Omega City"
    book7 = "Wing & Claw"
    book8 = "The Copernicus Legacy"
    book9 = "The Thickety"
    book10 = "The Doldrums"

    Please enter the number denoted to the book when issuing or returning.

    ''')

    g = int(input("Do you want to access Digital Library Book Maintenance System ? Press 1 if Yes or 2 if No: "))

    if g == 1 :

        def Available_Books () :
            for i in range (1, 11) :
                if book_lib.get(f"book{i}") == 's' :
                    print(f"Book{i} is available.\n")
                elif book_lib.get(f"book{i}") == 't' :
                    print(f"Book{i} is not available.\n")

        def Borrow_Book (z) :
            if book_lib.get(f"book{z}") == 's' :
                print("The book is available.")
                k = int(input("Do you want to issue it ? Press 1 if Yes or 2 if No: "))

                if k == 1 :
                    book_lib_update = {
                        f"book{z}" : 't'
                    }
                    book_lib.update(book_lib_update)
                    print("The book has been issued successfully !!")

                elif k == 2 :
                    print('Thank you for Enquiry.')

                else :
                    print("Incorrect Input ! Please try again.")

            else :
                print("The book is not available.")

        def Return_Book (y) :

            if book_lib.get(f"book{y}") == 's' :
                print('''The book must already be present in the library. 
                         Please contact Coordinator if book is with you.''')

            else :
                n = int(input("Do you want to return the book ? Press 1 if Yes or 2 if No: "))
                if n == 1 :
                    book_lib_update = {
                        f"book{y}" : 's'
                    }
                    book_lib.update(book_lib_update)
                    print("The book has been returned successfully !!")

                elif n == 2 :
                    print('Ok, please return the book wo=ithin time period.')

                else :
                    print("Incorrect Input ! Please try again.")

        p = int(input('''
        Press 1 to See the Available Books in the Library.
        Press 2 to Issue a Book
        Press 3 to Return a Book
        '''))

        if p == 1 :
            Available_Books()

        elif p == 2 :
            q = int(input("Enter the book number you want to issue: "))
            Borrow_Book(q)

        elif p == 3 :
            q = int(input("Enter the book number you want to return: "))
            Return_Book(q)

        else :
            print("Incorrect Input ! Please try again.") 

    elif g == 2 :
        print("Ok Thank You")

    else :
        print("Incorrect Input ! Please try again.")

       