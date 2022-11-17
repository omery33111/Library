from project import app, db



# ---------- User Class ---------- #

class Users(db.Model):
    user_id = db.Column("UserID", db.Integer, primary_key = True)
    user_name = db.Column("UserName", db.String(25), nullable = False)
    age = db.Column("Age", db.Integer, nullable = False)
    city = db.Column("City", db.String(25), nullable = False)
    user_to_loan = db.relationship("Loans", backref = "Users", lazy = True)

    def __init__(self, user_name, age, city):
        self.user_name = user_name
        self.age = age
        self.city = city

# ---------- User Class ---------- #



with app.app_context():
    db.create_all()



# ---------------------------------------------------------------------------------------------------- #