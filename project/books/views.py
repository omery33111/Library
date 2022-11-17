from flask import Blueprint, render_template, request, redirect
from project.books.models import Books
from project import db



books = Blueprint('books', __name__, template_folder = 'templates', url_prefix = '/books')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Book's Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ---------- DISPLAY:
@books.route("/", methods = ["GET"])
@books.route("/<id>")
def Book_display(id = -1):
    All_Books = []
    if int(id) <= -1:
        for book in Books.query.all():
            All_Books.append({"book_id": book.book_id,
                            "book_name": book.book_name,
                            "author": book.author,
                            "published": book.published,
                            "loantype": book.loantype})     # DISPLAY ALL BOOKS.
        return All_Books
    if int(id) > -1:
        book = Books.query.get(int(id))
        All_Books.append({"book_id": book.book_id,
                            "book_name": book.book_name,
                            "author": book.author,
                            "published": book.published,
                            "loantype": book.loantype})          # DISPLAY BOOK BY ID.
        return All_Books


# ---------- SEARCH:
@books.route("/booksearch", methods = ["POST"])
def Book_search(name = ""):
    name = request.form["booksearch"]
    book = Books.query.filter(Books.book_name == name).first()          # CHECK IF BOOK'S NAME MATCHES FORM'S NAME.
    if book is None:
        return redirect("/books")
    return redirect("/books/" + str(book.book_id))          # REDIRECTING TO Book_display FUNCTION WITH FILTERED BOOK'S ID, USING LINE #20 TO DISPLAY BOOK BY ID.



# ---------- ADD:
@books.route("/bookadd", methods = ["GET", "POST"])
def Book_add():
    if request.method == "POST":
        book_name = request.json["book_name"]
        author = request.json["author"]
        published = request.json["published"]
        loantype = request.json["loantype"]

        new_book = Books(book_name, author, published, loantype)            # VARIABLE FOR ALL USED FORMS.
        db.session.add(new_book)            # ADD NEW BOOK TO DATABASE.
        db.session.commit()
        return redirect("/books")
    return render_template("bookadd.html")


# ---------- DELETE:
@books.route("/bookdelete/<id>", methods = ["DELETE", "GET"])
def Book_delete(id = -1):
    db.session.delete(Books.query.get(id))          # DELETE BOOK BY ID.
    db.session.commit()
    return redirect("/books")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Book's Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #