from flask import render_template, Blueprint
from project.books.models import Books



core = Blueprint('core', __name__, template_folder = 'templates')




@core.route('/')
def index():
    return render_template('Books.html', books = Books.query.all())         # SETTING BOOK DISPLAY PAGE AS HOMEPAGE.



# ---------------------------------------------------------------------------------------------------- #