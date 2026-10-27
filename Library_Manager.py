import pickle
import os
class Book:
    total_books = 0
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.__year = year
        Book.total_books += 1
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,new_year):
        if new_year > 0:
            self.__year = new_year
        else:
            print("Error: Year must be positive!")
    @staticmethod
    def show_total_books():
        print(f"Total books in library: {Book.total_books}")
library = []
if os.path.exists("library.pkl"):
    with open("library.pkl", "rb") as f:
        library = pickle.load(f)
    print(f"Loaded {len(library)} books from file.")

while True:
    choice = input("1.Add Book\n2.Show All Books\n3.Exit & Save\nChoose One Option:")
    if choice == "1":
        t = input("Enter Book's Title:")
        a = input("Enter Book's Author:")
        y = int(input("Enter Book's Year:"))
        option1_result = Book(t,a,y)
        library.append(option1_result)
        print("Book aded successfully!")
        print("*" * 20)
    elif choice == "2":
        if not library:
            print("Library is empty!")
        else:
            for item in library:
                print(f"Title: {item.title}\nAuthor: {item.author}\n Year: {item.year}")
                Book.show_total_books()
        print("*" * 20)
    elif choice == "3":
        with open("library.pkl", "wb") as f:
            pickle.dump(library,f)
        print("Data savaed. Goodbye!")
        break
    else:
        print("Invalid option. Please try again!")
print("*" * 20)