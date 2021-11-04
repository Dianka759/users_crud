from flask import render_template,redirect,request

from flask_app import app

from flask_app.models.user import User


@app.route('/')
def index():
    users = User.get_all()
    return render_template("Read(All).html", all_users = users)

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect("/")

@app.route("/new_user")
def new_user():
    users = User.get_all()
    return render_template("Create.html", all_users = users)


@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        "id":id
    }
    user = User.get_user(data)
    return render_template("users_edit.html",user=user)


@app.route("/show/<int:id>")
def show_user(id):
    data = {
        "id":id
    }
    user = User.get_user(data)
    return render_template("Users_Read_One.html", user=user)


@app.route("/update/<int:id>",methods=["POST"])
def update(id):
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "id":id
    }
    User.edit_user(data)
    return redirect(f"/show/{id}")


@app.route("/delete/<int:id>")
def delete_user(id):
    data = {
        "id":id
    }
    User.delete_user(data)
    return redirect("/")


