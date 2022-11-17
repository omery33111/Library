from project import app, db



# ---------- Loan Class ---------- #

class Loans(db.Model):
    loan_id = db.Column("LoanID", db.Integer, primary_key = True)
    user_id = db.Column("UserID", db.Integer, db.ForeignKey("users.UserID"))
    book_id = db.Column("BookID", db.Integer, db.ForeignKey("books.BookID"))
    loandate = db.Column("LoanDate", db.Date, nullable = False)
    returndate = db.Column("ReturnDate", db.Date, nullable = False)
    returned = db.Column("ReturnedLoans", db.Boolean, nullable = False)

    def __init__(self, user_id, book_id, loandate, returndate):
        self.user_id = user_id
        self.book_id = book_id
        self.loandate = loandate
        self.returndate = returndate
        self.returned = False

# ---------- Loan Class ---------- #



with app.app_context():
    db.create_all()



# ---------------------------------------------------------------------------------------------------- #