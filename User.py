from Catalog import Catalog
class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id

    def showBooks(self):
        Catalog.displayAllBooks()



class Member(User):
    members=[]
    whoissuedbook={}
    @classmethod
    def  addMembers(cls,member):
        cls.members.append(member)

    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issuedBooks={}
        self.booksissued={}
        Member.members.append(name)

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    def SearchByName(self,name):
        book=Catalog.searchByName(name)
        return book

    def SearchByAuthor(self,author):
        book=Catalog.searchByAuthor(author)
        return book

    # assume name is unique
    def issueBook(self, name, date,month):
        actualtime=self.calculatetime(date,month)
        if len(self.issuedBooks)==3:
            return "You already issued maximum no. of books"
        else:
            if Catalog.searchByName(name):
                Catalog.removeBook(name)
                self.booksissued[name]=[date,month]
                self.issuedBooks[name]=actualtime
                Member.whoissuedbook[name] = self.name
                return "You can now collect your issued book "


    def returnBook(self, name,author, publish_date, pages,date,month):

        actualtime=self.calculatetime(date,month)
        if (actualtime-self.issuedBooks[name])>10:
            fine=((actualtime-self.issuedBooks[name])-10)*5
            print("***************Warning****************")
            print("please give fine of rupees"+str(fine))
            print("**************************************")
        Catalog.addBook(name,author,publish_date,pages)
        del Member.whoissuedbook[name]
        del self.issuedBooks[name]
        del self.booksissued[name]

        return "Book sucessfully returned"

    @staticmethod
    def calculatetime(date,month):
        if month>8 and month%2==1:
            final=date+month*31
        elif month in range(8,13) and month%2==0:
            final=date+month*31
        elif month==2:
            final=date+month*28
        else:
            final = date+month*30
        return final






    def issuedbook(self):
        print("u have issued book ")
        return  self.booksissued
    @classmethod
    def whoissued(cls):
        return cls.whoissuedbook


class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id

    def __repr__(self):
        return self.name + "  of  " + self.location + ' with emp id ' + self.emp_id

    def addBook(self, name, author, publish_date, pages):
        Catalog.addBook(name, author, publish_date, pages)
        print("BOOK ARE ADDED SUCESSFULLY")

    def removeBook(self, name):
        Catalog.removeBook(name)
        print("BOOK IS REMOVED SUCESSFULLY")

    def addMember(self,name,location,age,aadhar_id,student_id):
        Member(name,location,age,aadhar_id,student_id)

    def Members(self):
        for member in Member.members:
            print(member)

    def SearchMemberByName(self,name):
        for member in Member.members:
            if member == name:
                print(member)

    def issuedbymember(self):
        v=Member.whoissued()
        return v



    def removeBookItemFromCatalog(self, catalog, book, isbn):
        catalog.removeBookItem(book,isbn)
