from project import app, db



# ---------- Book Class ---------- #

class Books(db.Model):
    book_id = db.Column("BookID", db.Integer, primary_key = True)
    book_name = db.Column("BookName", db.String(25), nullable = False)
    author = db.Column("Author", db.String(25), nullable = False)
    published = db.Column("PublishDate", db.Integer, nullable = False)
    loantype = db.Column("LoanType", db.Integer, nullable = False)
    book_to_loan = db.relationship("Loans", backref = "Books", lazy = True)
    
    def __init__(self, book_name, author, published, loantype):
        self.book_name = book_name
        self.author = author
        self.published = published
        self.loantype = loantype

# ---------- Book Class ---------- #



with app.app_context():
    db.create_all()



# ---------------------------------------------------------------------------------------------------- #