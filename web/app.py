from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")
mydb = client["mydatabase"]
mycol = mydb["mycollection"]

@app.route("/")
def main():
    return render_template("index.html", data=mycol.find())

@app.route("/add", methods=["POST"])
def add_comment():
    ip = request.form.get("ip")
    username = request.form.get("username")
    passwd = request.form.get("passwd")

    if ip and username and passwd:
        mycol.insert_one({"ip": ip, "username":username, "passwd":passwd})
    return redirect(url_for("main"))

@app.route("/delete", methods=["POST"])
def delete_comment():
    try:
        idx = int(request.form.get("idx"))
        if 0 <= idx < len(mycol.find()):
            mycol.delete_one(idx)
    except Exception:
        pass
    return redirect(url_for("main"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)