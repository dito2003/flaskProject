from flask import Flask, render_template,flash , redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loginregform.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(seconds=40)
db = SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        session["client"] = uname
        return redirect(url_for("mainPage"))
        login = user.query.filter_by(username=uname, password=passw).first()
        if not user (user.password, password):
            return redirect(url_for('login'))
            return redirect(url_for('info'))
        else:
            if 'client' in session:
                return redirect(url_for('info'))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        email = request.form['email']
        passw = request.form['passw']

        register = user(username=uname, email=email, password=passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)