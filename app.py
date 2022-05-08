from flask import Flask, render_template, request, redirect
from db import *


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html", data=data)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        id = request.form["id"]
        password = request.form["password"]
        add_data(data, name, id, password)
        return redirect("/")        
    return render_template("add.html")

@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        index = request.form['index']
        name = request.form["name"]
        id = request.form["id"]
        password = request.form["password"]
        update_data(data, index, name, id, password)
        return redirect("/")    
    return render_template("update.html")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        index = request.form['index']
        delete_data(data, index)
        return redirect("/")  
    return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug=True)