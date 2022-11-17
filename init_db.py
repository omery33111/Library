from datetime import date

from project import db, app
from project.users.models import Users
from project.books.models import Books
from project.loans.models import Loans



# -------------------------------------------------------------------------------------------------------------- #

# ---------- USERS:
user1 = Users(user_name = "Gary Chase", age = 37, city = "New Yelnenya")
user2 = Users(user_name = "Mylee Good", age = 23, city = "Port Fayette")
user3 = Users(user_name = "Kennedy Wilkins", age = 52, city = "Wlandtruthky")
user4 = Users(user_name = "Lana Gray", age = 41, city = "New Rniapagnti")
user5 = Users(user_name = "Cayson Warren", age = 27, city = "Ckyrden")
user6 = Users(user_name = "Tyson Sosa", age = 19, city = "Frepphia")
user7 = Users(user_name = "Reginald Daniels", age = 25, city = "Bluport")
user8 = Users(user_name = "Cayson Warren", age = 33, city = "Klurbus")


# ---------- BOOKS:
book1 = Books(book_name = "Phantom Of Sorrow", author = "Darragh Alcock", published = 2008, loantype = 1)
book2 = Books(book_name = "Agent With Gold", author = "Gaia Hatfield", published = 2002, loantype = 2)
book3 = Books(book_name = "Creators With Strength", author = "Eduardo Middleton", published = 2010, loantype = 3)
book4 = Books(book_name = "Bandits Of Greatness", author = "Harlen Sharpe", published = 2012, loantype = 1)
book5 = Books(book_name = "Pilots And Rebels", author = "Dolcie Sweeney", published = 2006, loantype = 2)
book6 = Books(book_name = "Butcher Of The Land", author = "Astrid Lang", published = 2011, loantype = 3)
book7 = Books(book_name = "Giant Of The Sea", author = "Stan Bassett", published = 2015, loantype = 1)
book8 = Books(book_name = "Friends And Creators", author = "Charlize Powell", published = 2004, loantype = 2)


# ---------- LOANS:
loan1 = Loans(user_id = 8, book_id = 1, loandate = date(2022, 10, 22), returndate = date(2022, 11, 1))
loan2 = Loans(user_id = 7, book_id = 2, loandate = date(2022, 10, 28), returndate = date(2022, 11, 2))
loan3 = Loans(user_id = 6, book_id = 3, loandate = date(2022, 11, 1), returndate = date(2022, 11, 3))
loan4 = Loans(user_id = 5, book_id = 4, loandate = date(2022, 10, 21), returndate = date(2022, 10, 31))
loan5 = Loans(user_id = 4, book_id = 5, loandate = date(2022, 11, 4), returndate = date(2022, 11, 9))
loan6 = Loans(user_id = 3, book_id = 6, loandate = date(2022, 11, 9), returndate = date(2022, 11, 11))
loan7 = Loans(user_id = 2, book_id = 7, loandate = date(2022, 11, 13), returndate = date(2022, 11, 23))
loan8 = Loans(user_id = 1, book_id = 8, loandate = date(2022, 11, 15), returndate = date(2022, 11, 20))



with app.app_context():
    db.session.add_all([user1, user2, user3, user4, user5, user6, user7, user8])
    db.session.add_all([book1, book2, book3, book4, book5, book6, book7, book8])
    db.session.add_all([loan1, loan2, loan3, loan4, loan5, loan6, loan7, loan8])

    db.session.commit()



# -------------------------------------------------------------------------------------------------------------- #