from Book import Book


# First Book is file & second is Class

class Catalog:
    different_book_count = 0
    books = []
    booksname={}


    @classmethod
    def addBookslist(cls,book):
        cls.books.append(book)

    def addBook(name, author, publish_date, pages):
        b = Book(name, author, publish_date, pages)
        Catalog.booksname[author]=name

        Catalog.different_book_count += 1
        Catalog.books.append(b)
        return b

    # Only available to admin
    def addBookItem(book, isbn, rack):
        book.addBookItem(isbn, rack)

    def searchByName(name):
        for book in Catalog.books:
            if name.strip() == book.name:
                return book
            else:
                return "Sorry!!No book is available with this name"

    def searchByAuthor(author):
        if author in Catalog.booksname:
            return Catalog.booksname[author]
        else:
            return "Sorry!!No book is available with this Author"

    def displayAllBooks():
        print('Different Book Count', Catalog.different_book_count)
        c = 0
        for book in Catalog.books:
            c += book.total_count
            book.printBook()

        print('Total Book Count', c)

    def removeBookItem(name, isbn):
        book =Catalog.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)

    def removeBook(name):
        for book in Catalog.books:
            if book.name==name:
                Catalog.books.remove(book)
