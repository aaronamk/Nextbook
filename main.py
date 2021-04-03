from urllib.parse import quote_plus
from flask import Flask, redirect, url_for, request


nextbook = Flask(__name__)


@nextbook.route("/", methods = ['POST', 'GET'])
def search():
    if request.method == "POST":
        phrase = quote_plus(request.form["phrase"])
        filter = quote_plus(request.form["filter"])
        return redirect(f"search?filter={filter}&q={phrase}")
    else:
        test = request.args.get("phrase")
        test = request.args.get("filter")
        filter = request.form["filter"]
        return redirect("asdf")


@nextbook.route("/search")
def results():
    return " | ".join(f"{k}: {v}" for k, v in request.args.items())


@nextbook.route("/class-list")
def class_list():
    return "full list"


@nextbook.route("/add-book")
def add_book():
    return "add a book"


@nextbook.route("/about")
def about():
    return "We are cool bros!"


if __name__ == "__main__":
    nextbook.run()
