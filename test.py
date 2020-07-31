from Book import Book
from Catalog import Catalog
from User import Member, Librarian
#to add librarian
lib=Librarian("Kishan Mohanty","Bangalore","23","16627372","DDsl865")
print("\n")
#to check librarian detail
print(lib)
print("\n")
#to add book
b = Catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
Catalog.addBookItem(b, '123hg','H1B2')
Catalog.addBookItem(b, '124hg','H1B4')
Catalog.addBookItem(b, '125hg','H1B5')

b = Catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
Catalog.addBookItem(b, '463hg','K1B2')
lib.addBook("VIJAYPATH","Akash","1970",318)
lib.addBook("HAlFGIRLFRIEND","CHETAN BHAGAT","2014",777)

#to display book
Catalog.displayAllBooks()
print("\n")
lib.showBooks()
print("\n")

#to remove book
Catalog.removeBookItem('Shoe Dog','124hg')
lib.removeBook("HALFGIRLFRIEND")


#check removal
lib.showBooks()
print("\n")

#back to same
lib.addBook("HAlFGIRLFRIEND","CHETAN BHAGAT","2014",777)



#add member
m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')
Anisha=Member("Anisha","Balasore",23,"61465165156","KMAD2105")
Raja=Member("Raja","Balasore",23,"614651651896","KMAD4505")

#search memberby name
print("\n")
lib.SearchMemberByName("Anisha")
print(m1)
lib.SearchMemberByName("Raja")



#issuebook
print("\n")
print(Raja.issueBook("HAlFGIRLFRIEND",21,8))

#CHANGES AFTER ISSUING THE BOOK
#check book issue by member
print("\n")
print(Raja.issuedbook())


#bookissuedbymember
print("********")
print(lib.issuedbymember())
print("******")




#return book and check fine
print(Raja.returnBook("HAlFGIRLFRIEND","CHETAN BHAGAT","2014",777,18,11))

#catalog after return book
print(Raja.issuedbook())
print("********")
print(lib.issuedbymember())
print("******")

#search by author
print(Raja.SearchByAuthor("CHETAN BHAGAT"))



