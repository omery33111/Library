from flask import Blueprint, render_template, request, redirect
from project.users.models import Users
from project import db



users = Blueprint('users', __name__, template_folder = 'templates', url_prefix = '/users')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ User's Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ---------- DISPLAY:
@users.route("/", methods = ["GET"])
@users.route("/<id>")
def User_display(id = -1):
    All_Users = []
    if int(id) <= -1:
        for user in Users.query.all():
            All_Users.append({"user_id": user.user_id,
                            "user_name": user.user_name,
                            "age": user.age,
                            "city": user.city})     # DISPLAY ALL Users.
        return All_Users
    if int(id) > -1:
        user = Users.query.get(int(id))
        All_Users.append({"user_id": user.user_id,
                            "user_name": user.user_name,
                            "age": user.age,
                            "city": user.city})          # DISPLAY Users BY ID.
        return All_Users


# ---------- SEARCH:
@users.route("/usersearch", methods = ["POST"])
def User_search(name = ""):
    name = request.form["usersearch"]
    user = Users.query.filter(Users.user_name == name).first()          # CHECK IF USER'S NAME MATCHES FORM'S NAME.
    if user is None:
        return redirect("/users")
    return redirect("/users/" + str(user.user_id))          # REDIRECTING TO User_display FUNCTION WITH FILTERED USER'S ID, USING LINE #20 TO DISPLAY USER BY ID.


# ---------- ADD:
@users.route("/useradd", methods = ["GET", "POST"])
def User_add():
    if request.method == "POST":
        user_name = request.json["user_name"]
        age = request.json["age"]
        city = request.json["city"]

        new_user = Users(user_name, age, city)            # VARIABLE FOR ALL USED FORMS.
        db.session.add(new_user)            # ADD NEW USER TO DATABASE.
        db.session.commit()
        return redirect("/users")
    return render_template('useradd.html')


# ---------- DELETE:
@users.route("/userdelete/<id>", methods = ["DELETE", "GET"])
def User_delete(id = -1):
    db.session.delete(Users.query.get(id))          # DELETE USER BY ID.
    db.session.commit()
    return redirect("/users")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ User's Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #