from flask import Blueprint, render_template, request, redirect
from datetime import datetime, timedelta

from project.loans.models import Loans
from project.books.models import Books
from project import db



loans = Blueprint('loans', __name__, template_folder = 'templates', url_prefix = '/loans')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Loan's Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ---------- DISPLAY:
@loans.route("/", methods = ["GET"])
def Loan_display():
    All_Loans = []
    for loan in Loans.query.all():
        All_Loans.append({"loan_id": loan.loan_id,
                            "user_id": loan.user_id,
                            "book_id": loan.book_id,
                            "loandate": loan.loandate,
                            "returndate": loan.returndate})     # DISPLAY ALL Loans.
    return All_Loans


# ---------- LOAN A BOOK:
@loans.route("/loanadd", methods = ["GET", "POST"])
def Loan_add():
    dateloned = datetime.utcnow().date()            # SETTING LOAN DATE AS TODAY.

    if request.method == "POST":
        for book in Books.query.filter_by(book_id = request.json.get("book_id")):           # FOR BOOK, SETTING BOOK'S ID FROM ALL BOOKS TO REQUESTED FORM'S BOOK ID.
            if book.book_id == int(request.json.get("book_id")):            # CHECK IF REQUESTED BOOK ID EXISTS.
                if book.loantype == 1: returndate = dateloned + timedelta(days = 10)
                elif book.loantype == 2: returndate = dateloned + timedelta(days = 5)
                else: returndate = dateloned + timedelta(days = 2)                      # LINES #30-32 - SETTING RETURN DATE BY FILTERING BOOK'S LOAN TYPE AND CALCULATING TODAY'S DATE TO BOOK'S LOAN TERMS.


            New_loan = Loans(user_id = request.json["user_id"],         # VARIABLE ALL USED FORMS.
                            book_id = request.json["book_id"],
                            loandate = dateloned,
                            returndate = returndate)
            db.session.add(New_loan)            # ADD NEW LOAN TO DATABASE.
            db.session.commit()
            return redirect("/loans")
    return render_template("loanadd.html")


# ---------- LOAN RETURN:
@loans.route("/loanreturn/<id>", methods = ["DELETE", "GET"])
def Loan_return(id = -1):
        db.session.delete(Loans.query.get(id))          # RETURN LOAN, DELETE LOAN FROM DATABESE BY ID.
        db.session.commit()
        return redirect("/loans")


# ---------- LATE LOANS:
@loans.route("/loanlate", methods = ["GET"])
def Loan_late():
    late_loans = []
    active_loans = Loans.query.filter_by(returned = False)          # SETTING VARIABLE FOR ALL LOANS THAT NOT RETURNED YET.
    for loan in active_loans:           # PULLING ONE LOAN IN ALL ACTIVE LOAN LIST.
        if datetime.today().date() > loan.returndate:           # SEARCHING FOR LOANS THAT TODAY'S DATE IS IT'S LIMIT.
            late_loans.append({"loan_id": loan.loan_id,
                            "user_id": loan.user_id,
                            # "user_name": loan.user_name,
                            "book_id": loan.book_id,
                            # "book_name": loan.book_name,
                            "loandate": loan.loandate,
                            "returndate": loan.returndate})         # ADDING FOUND LOANS TO LATE LOANS ARRAY.
    return late_loans            # DISPLAY LATE LOANS.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Loan's Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# #`<div>LoanID ${singleLoan["loan_id"]}<br> 
#                   UserID ${singleLoan["user_id"]}<br>
#                   UserName ${singleLoan["user_name"]}<br>
#                   BookID ${singleLoan["book_id"]}<br>
#                   BookName ${singleLoan["book_name"]}<br>
#                   LoanDate ${singleLoan["loandate"]}<br>
#                   LoanReturn ${singleLoan["returndate"]}<br>